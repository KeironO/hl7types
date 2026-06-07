from __future__ import annotations

import importlib
import typing
import warnings
from typing import Any, get_type_hints
from xml.etree import ElementTree as ET

from pydantic import BaseModel

from hl7types._utils import version_to_module
from hl7types.codecs.er7.encoder import DELIM_DEF, SEG_ALIAS_RE, EncodingChars
from hl7types.registry import HL7Registry

_HL7_XML_NS = "urn:hl7-org:v2xml"
_NS_PREFIX = f"{{{_HL7_XML_NS}}}"


def _is_model(cls: Any) -> bool:
    try:
        return isinstance(cls, type) and issubclass(cls, BaseModel)
    except TypeError:
        return False


def _unwrap(annotation: Any) -> tuple[Any, bool]:
    origin = typing.get_origin(annotation)
    args = typing.get_args(annotation)
    if origin is typing.Union:
        non_none = [a for a in args if a is not type(None)]
        if len(non_none) == 1:
            return _unwrap(non_none[0])
        return annotation, False
    if origin is list:
        inner: Any = args[0] if args else Any
        inner_origin = typing.get_origin(inner)
        inner_args = typing.get_args(inner)
        if inner_origin is typing.Union:
            non_none = [a for a in inner_args if a is not type(None)]
            if non_none:
                inner = non_none[0]
        return inner, True
    return annotation, False


def _is_segment_cls(cls: Any) -> bool:
    if not _is_model(cls):
        return False
    for fi in cls.model_fields.values():
        alias = fi.serialization_alias
        if isinstance(alias, str) and SEG_ALIAS_RE.match(alias):
            return True
    return False


def _local(tag: str) -> str:
    """Strip Clark-notation namespace prefix from an element tag."""
    return tag[len(_NS_PREFIX) :] if tag.startswith(_NS_PREFIX) else tag


def _group_xml_tag(cls: type) -> str:
    """ADT_A01_PROCEDURE to ADT_A01.PROCEDURE (mirrors the encoder)."""
    name = cls.__name__
    idx = name.rfind("_")
    return f"{name[:idx]}.{name[idx + 1 :]}" if idx != -1 else name


def _extract_truncation(root: ET.Element) -> str:
    """Read MSH.2 and MSH.12/VID.1 from an XML message root and return the
    truncation character (empty string if none or pre-v2.7)."""
    ns = _NS_PREFIX

    msh_elem = root.find(f"{ns}MSH")
    if msh_elem is None:
        msh_elem = root.find("MSH")
    if msh_elem is None:
        return ""

    def _find(elem: ET.Element, tag: str) -> ET.Element | None:
        r = elem.find(f"{ns}{tag}")
        return r if r is not None else elem.find(tag)

    msh2_elem = _find(msh_elem, "MSH.2")
    msh2 = (msh2_elem.text or "").strip() if msh2_elem is not None else ""
    if len(msh2) != 5:
        return ""

    vid1_parent = _find(msh_elem, "MSH.12")
    if vid1_parent is not None:
        vid1_elem = _find(vid1_parent, "VID.1")
        version = (vid1_elem.text or "").strip() if vid1_elem is not None else ""
    else:
        version = ""

    if not version:
        return ""

    try:
        enc = EncodingChars.from_msh2(msh2, version)
        return enc.truncation
    except ValueError:
        return ""


def _build_alias_map(seg_cls: type[BaseModel]) -> dict[str, tuple[str, Any, bool]]:
    """Map serialization_alias to (fname, base_type, is_list) for a segment."""
    hints = get_type_hints(seg_cls)
    result: dict[str, tuple[str, Any, bool]] = {}
    for fname, fi in seg_cls.model_fields.items():
        alias = fi.serialization_alias
        if not isinstance(alias, str):
            continue
        ann = hints.get(fname)
        if ann is None:
            continue
        base_type, is_list = _unwrap(ann)
        result[alias] = (fname, base_type, is_list)
    return result


def _strip_truncation(value: str, truncation: str) -> str:
    if truncation and value.endswith(truncation):
        return value.rstrip(truncation)
    return value


def _decode_composite(
    elem: ET.Element,
    cls: type[BaseModel],
    truncation: str = "",
) -> dict[str, Any]:
    """Decode a composite datatype element into a dict suitable for model_validate."""
    alias_map = _build_alias_map(cls)
    data: dict[str, Any] = {}
    for child in elem:
        tag = _local(child.tag)
        if tag not in alias_map:
            continue
        fname, base_type, is_list = alias_map[tag]
        if _is_model(base_type):
            val: Any = _decode_composite(child, base_type, truncation)
        else:
            val = _strip_truncation((child.text or "").strip(), truncation)
        if is_list:
            data.setdefault(fname, [])
            data[fname].append(val)
        else:
            data[fname] = val
    return data


def decode_xml_segment(
    elem: ET.Element,
    seg_cls: type[BaseModel],
    *,
    strict: bool = False,
    truncation: str = "",
) -> BaseModel:
    """Decode a single XML segment element into a typed segment model.

    Parameters
    ----------
    elem : ET.Element
        The XML element representing the segment (e.g. ``<MSH>``).
    seg_cls : type[BaseModel]
        The segment model class to decode into.
    strict : bool, optional
        If ``True``, raises ``pydantic.ValidationError`` when required fields
        are absent. If ``False``, missing required fields are filled with empty
        placeholder values and a ``UserWarning`` is emitted. Defaults to
        ``False``.

    Returns
    -------
    BaseModel
        A validated instance of ``seg_cls``.

    Examples
    --------
    >>> from xml.etree import ElementTree as ET
    >>> from hl7types.hl7.v2_5_1.segments import MSA
    >>> from hl7types.codecs.xml.decoder import decode_xml_segment
    >>> elem = ET.fromstring('<MSA><MSA.1>AA</MSA.1><MSA.2>MSG001</MSA.2></MSA>')
    >>> seg = decode_xml_segment(elem, MSA)
    >>> seg.msa_1
    'AA'
    """
    seg_name = seg_cls.__name__
    alias_map = _build_alias_map(seg_cls)

    # Group children by tag so repeating fields collect all occurrences.
    children_by_tag: dict[str, list[ET.Element]] = {}
    for child in elem:
        tag = _local(child.tag)
        children_by_tag.setdefault(tag, []).append(child)

    data: dict[str, Any] = {}

    # MSH.2 / FHS.2 / BHS.2 are the encoding character definitions. Never strip them!
    delim_encoding_alias = f"{seg_name}.2" if seg_name in DELIM_DEF else ""

    for alias, (fname, base_type, is_list) in alias_map.items():
        children = children_by_tag.get(alias)
        if not children:
            continue

        trunc = "" if alias == delim_encoding_alias else truncation

        if is_list:
            items: list[Any] = []
            for child in children:
                if _is_model(base_type):
                    items.append(_decode_composite(child, base_type, trunc))
                else:
                    items.append(_strip_truncation((child.text or "").strip(), trunc))
            if items:
                data[fname] = items
        else:
            child = children[0]
            if _is_model(base_type):
                val = _decode_composite(child, base_type, trunc)
                if val:
                    data[fname] = val
            else:
                text = _strip_truncation((child.text or "").strip(), trunc)
                if text:
                    data[fname] = text

    # MSH.1 (field separator) is an attribute of the encoding, not a child element.
    # The XML format omits it; inject the standard value so model_validate succeeds.
    if (
        seg_name in DELIM_DEF
        and "msh_1" not in data
        and "fhs_1" not in data
        and "bhs_1" not in data
    ):
        for fname, fi in seg_cls.model_fields.items():
            alias = fi.serialization_alias
            if isinstance(alias, str) and alias.endswith(".1"):
                if fi.is_required() and fname not in data:
                    data[fname] = "|"
                break

    if not strict:
        skipped: list[str] = []
        for fname, fi in seg_cls.model_fields.items():
            if fname in data or not fi.is_required():
                continue
            hints = get_type_hints(seg_cls)
            ann = hints.get(fname)
            if ann is None:
                continue
            base_type, is_list = _unwrap(ann)
            skipped.append(fname)
            if is_list:
                data[fname] = []
            elif _is_model(base_type):
                data[fname] = {}
            else:
                data[fname] = ""

        if skipped:
            warnings.warn(
                f"Lenient XML decoding skipped missing required field(s) "
                f"on segment {seg_name}: {', '.join(skipped)}. "
                "Placeholder values were injected because strict=False.",
                UserWarning,
                stacklevel=2,
            )

    return seg_cls.model_validate(data)


def _decode_struct(
    elem: ET.Element,
    model_cls: type[BaseModel],
    *,
    strict: bool = False,
    registry: HL7Registry | None = None,
    truncation: str = "",
) -> BaseModel | None:
    """Recursively decode an XML element into a message/group/segment model."""
    if _is_segment_cls(model_cls):
        resolved = (
            registry.get_segment(model_cls.__name__)
            if registry and registry.get_segment(model_cls.__name__) is not None
            else None
        ) or model_cls
        return decode_xml_segment(elem, resolved, strict=strict, truncation=truncation)

    hints = get_type_hints(model_cls)
    data: dict[str, Any] = {}

    # Index direct children by their local tag name for O(1) lookup.
    # Multiple children with the same tag are preserved as a list.
    children_by_tag: dict[str, list[ET.Element]] = {}
    for child in elem:
        tag = _local(child.tag)
        children_by_tag.setdefault(tag, []).append(child)

    for fname in model_cls.model_fields:
        ann = hints.get(fname)
        if ann is None:
            continue
        base_type, is_list = _unwrap(ann)
        if not _is_model(base_type):
            continue

        resolved_type = (
            registry.get_segment(base_type.__name__)
            if registry and _is_segment_cls(base_type) and registry.get_segment(base_type.__name__)
            else None
        ) or base_type

        # Determine the XML tag this field maps to.
        # Segments use their class name; groups use the dot-notation tag.
        if _is_segment_cls(resolved_type):
            xml_tag = resolved_type.__name__
        else:
            xml_tag = _group_xml_tag(resolved_type)

        matching = children_by_tag.get(xml_tag, [])

        if is_list:
            items: list[Any] = []
            for child_elem in matching:
                item = _decode_struct(
                    child_elem,
                    resolved_type,
                    strict=strict,
                    registry=registry,
                    truncation=truncation,
                )
                if item is not None:
                    items.append(item)
            if items:
                data[fname] = items
        else:
            if matching:
                item = _decode_struct(
                    matching[0],
                    resolved_type,
                    strict=strict,
                    registry=registry,
                    truncation=truncation,
                )
                if item is not None:
                    data[fname] = item

    if not data:
        return None

    if not strict:
        skipped: list[str] = []
        for fname, fi in model_cls.model_fields.items():
            if fname in data or not fi.is_required():
                continue
            ann = hints.get(fname)
            if ann is None:
                continue
            base_type, is_list = _unwrap(ann)
            if not _is_model(base_type):
                continue
            skipped.append(fname)
            data[fname] = [] if is_list else base_type.model_construct()

        if skipped:
            warnings.warn(
                f"Lenient XML decoding skipped missing required segment/group "
                f"field(s) on {model_cls.__name__}: {', '.join(skipped)}. "
                "Placeholder values were injected because strict=False.",
                UserWarning,
                stacklevel=2,
            )

    return model_cls.model_validate(data)


def _resolve_msg_cls_from_xml(
    root: ET.Element,
    registry: HL7Registry | None = None,
) -> type[BaseModel]:
    """Resolve the message class from the MSH segment inside an XML message element."""
    ns = _NS_PREFIX

    msh_elem = root.find(f"{ns}MSH")
    if msh_elem is None:
        msh_elem = root.find("MSH")
    if msh_elem is None:
        raise ValueError("No MSH element found in XML; cannot auto-detect message type")

    def _find(elem: ET.Element, tag: str) -> ET.Element | None:
        result = elem.find(f"{ns}{tag}")
        if result is None:
            result = elem.find(tag)
        return result

    def _text(tag: str) -> str:
        child = _find(msh_elem, tag)
        return (child.text or "").strip() if child is not None else ""

    def _sub_text(parent_tag: str, child_tag: str) -> str:
        parent = _find(msh_elem, parent_tag)
        if parent is None:
            return ""
        child = _find(parent, child_tag)
        return (child.text or "").strip() if child is not None else ""

    msg_code = _sub_text("MSH.9", "MSG.1")
    trigger = _sub_text("MSH.9", "MSG.2")
    structure = _sub_text("MSH.9", "MSG.3")

    if not structure and msg_code and trigger:
        structure = f"{msg_code}_{trigger}"
    elif not structure:
        structure = msg_code

    if not structure:
        raise ValueError("MSH.9 is empty or missing; cannot auto-detect message type")

    vid_1 = _sub_text("MSH.12", "VID.1")
    version = vid_1 or _text("MSH.12")

    if not version:
        raise ValueError("MSH.12 is empty or missing; cannot auto-detect HL7 version")

    if registry:
        cls = registry.get_message(version, structure)
        if cls is not None:
            return cls

    mod_name = version_to_module(version)
    try:
        module = importlib.import_module(f"hl7types.hl7.{mod_name}.messages.{structure}")
        return getattr(module, structure)
    except (ModuleNotFoundError, AttributeError) as exc:
        raise ValueError(
            f"Unknown message structure {structure!r} for HL7 version {version!r}"
        ) from exc


def decode_xml(
    xml_string: str,
    msg_cls: type[BaseModel] | None = None,
    *,
    strict: bool = True,
    registry: HL7Registry | None = None,
) -> BaseModel:
    """Decode an HL7 v2 XML string into a typed message or segment model.

    When ``msg_cls`` is not provided, the message class is resolved
    automatically from ``MSH.9`` (message type) and ``MSH.12`` (version)
    inside the XML. Both namespaced (``urn:hl7-org:v2xml``) and bare XML are
    accepted.

    Parameters
    ----------
    xml_string : str
        A complete HL7 v2 XML string, including or excluding the XML
        declaration.
    msg_cls : type[BaseModel], optional
        The message or segment model class to decode into. If ``None``, the
        class is resolved dynamically from ``MSH.9`` and ``MSH.12``.
    strict : bool, optional
        If ``True``, raises ``pydantic.ValidationError`` when required fields
        or segments are absent. If ``False``, missing required fields are
        filled with empty placeholder values and a ``UserWarning`` is emitted.
        Defaults to ``True``.
    registry : HL7Registry, optional
        Registry of custom segment and message classes. Consulted when the
        decoder encounters a segment or message type not present in the
        generated specification models.

    Returns
    -------
    BaseModel
        A validated instance of the resolved or provided message/segment class.

    Raises
    ------
    ValueError
        If the XML string is empty, no MSH element is found, or the message
        type or version cannot be resolved to a known model class.
    pydantic.ValidationError
        If ``strict=True`` and required fields or segments are missing, or if
        any field value fails format validation.

    Examples
    --------
    >>> from hl7types.codecs.xml.decoder import decode_xml
    >>> xml = (
    ...     '<?xml version="1.0" encoding="UTF-8"?>'
    ...     '<ACK xmlns="urn:hl7-org:v2xml">'
    ...     '<MSH><MSH.1>|</MSH.1><MSH.2>^~\\\\&amp;</MSH.2>'
    ...     '<MSH.9><MSG.1>ACK</MSG.1></MSH.9>'
    ...     '<MSH.10>001</MSH.10>'
    ...     '<MSH.11><PT.1>P</PT.1></MSH.11>'
    ...     '<MSH.12><VID.1>2.5.1</VID.1></MSH.12>'
    ...     '<MSH.7><TS.1>20260101</TS.1></MSH.7>'
    ...     '</MSH>'
    ...     '<MSA><MSA.1>AA</MSA.1><MSA.2>001</MSA.2></MSA>'
    ...     '</ACK>'
    ... )
    >>> msg = decode_xml(xml)
    >>> msg.MSA.msa_1
    'AA'
    """
    if not xml_string or not xml_string.strip():
        raise ValueError("Empty XML string")

    try:
        root = ET.fromstring(xml_string)
    except ET.ParseError as exc:
        raise ValueError(f"Invalid XML: {exc}") from exc

    if msg_cls is None:
        # If the root element contains an MSH child it is a message; resolve
        # the class from MSH.9/MSH.12.  Otherwise it must be a bare segment
        # and the caller must supply msg_cls explicitly.
        has_msh = root.find(f"{_NS_PREFIX}MSH") is not None or root.find("MSH") is not None
        if not has_msh:
            root_tag = _local(root.tag)
            raise ValueError(
                f"Cannot auto-detect class for bare segment element {root_tag!r}; "
                "pass msg_cls explicitly."
            )
        msg_cls = _resolve_msg_cls_from_xml(root, registry=registry)

    truncation = _extract_truncation(root)

    # Single-segment shortcut: if msg_cls is a segment, decode the root element directly.
    if _is_segment_cls(msg_cls):
        return decode_xml_segment(root, msg_cls, strict=strict, truncation=truncation)

    result = _decode_struct(root, msg_cls, strict=strict, registry=registry, truncation=truncation)
    if result is None:
        raise ValueError(f"Could not decode XML as {msg_cls.__name__}")
    return result
