from __future__ import annotations

import importlib
import re
import typing
import warnings
from functools import lru_cache
from typing import Any, get_type_hints

from pydantic import BaseModel

from hl7types._utils import version_to_module
from hl7types.codecs.er7.encoder import (
    DEFAULT_ENCODING,
    DELIM_DEF,
    EncodingChars,
)
from hl7types.registry import HL7Registry

_UNESCAPE_MAP: dict[str, str] = {
    "F": "|",
    "S": "^",
    "T": "&",
    "R": "~",
    "E": "\\",
}


def _unescape(value: str, enc: EncodingChars) -> str:
    e = re.escape(enc.escape)
    result = re.sub(
        f"{e}([FSTRE]){e}",
        lambda m: _UNESCAPE_MAP.get(m.group(1), m.group(0)),
        value,
    )
    if enc.truncation and result.endswith(enc.truncation):
        result = result.rstrip(enc.truncation)
    return result


def _unwrap(annotation: Any) -> tuple[Any, bool]:
    """Unwrap Optional[List[X]] / Optional[X] / List[X] / X to (inner_type, is_list)."""
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


def _is_model(cls: Any) -> bool:
    try:
        return isinstance(cls, type) and issubclass(cls, BaseModel)
    except TypeError:
        return False


def is_segment_cls(cls: Any, registry: HL7Registry | None = None) -> bool:
    if not _is_model(cls):
        return False

    if ".segments." in getattr(cls, "__module__", ""):
        return True

    if registry is not None and registry.get_segment(cls.__name__) is cls:
        return True

    return False


@lru_cache(maxsize=256)
def _reachable_segment_names_standard(model_cls: type[BaseModel]) -> frozenset[str]:
    """Segment names reachable from model_cls using only the standard generated classes."""
    if is_segment_cls(model_cls):
        return frozenset({model_cls.__name__})
    names: set[str] = set()
    try:
        hints = get_type_hints(model_cls)
    except Exception:
        return frozenset()
    for fname in model_cls.model_fields:
        ann = hints.get(fname)
        if ann is None:
            continue
        base_type, _ = _unwrap(ann)
        if _is_model(base_type):
            names |= _reachable_segment_names_standard(base_type)
    return frozenset(names)


def _reachable_segment_names(
    model_cls: type[BaseModel],
    registry: HL7Registry | None = None,
) -> frozenset[str]:
    """Segment names reachable from model_cls, including registry-registered segments."""
    if registry is None:
        return _reachable_segment_names_standard(model_cls)
    if is_segment_cls(model_cls, registry):
        return frozenset({model_cls.__name__})
    names: set[str] = set()
    try:
        hints = get_type_hints(model_cls)
    except Exception:
        return frozenset()
    for fname in model_cls.model_fields:
        ann = hints.get(fname)
        if ann is None:
            continue
        base_type, _ = _unwrap(ann)
        if _is_model(base_type):
            names |= _reachable_segment_names(base_type, registry)
    return frozenset(names)


@lru_cache(maxsize=512)
def _build_pos_map(model_cls: type[BaseModel]) -> dict[int, tuple[str, Any, bool]]:
    hints = get_type_hints(model_cls)
    result: dict[int, tuple[str, Any, bool]] = {}
    for fname, fi in model_cls.model_fields.items():
        alias = fi.serialization_alias
        if not isinstance(alias, str):
            continue
        dot = alias.rfind(".")
        if dot == -1 or not alias[dot + 1 :].isdigit():
            continue
        pos = int(alias[dot + 1 :])
        ann = hints.get(fname)
        if ann is None:
            continue
        base_type, is_list = _unwrap(ann)
        result[pos] = (fname, base_type, is_list)
    return result


def _parse_rep(raw: str, field_type: Any, enc: EncodingChars) -> Any:
    if not raw:
        return None
    if not _is_model(field_type):
        return _unescape(raw, enc)

    components = raw.split(enc.component)
    pm = _build_pos_map(field_type)
    if not pm:
        return None

    result: dict[str, Any] = {}
    for pos, (fname, sub_type, _) in pm.items():
        if pos > len(components):
            continue
        raw_comp = components[pos - 1]
        if not raw_comp:
            continue
        if _is_model(sub_type):
            sub_pm = _build_pos_map(sub_type)
            sub_parts = raw_comp.split(enc.subcomponent)
            sub_result: dict[str, Any] = {}
            for spos, (sfname, _, _) in sub_pm.items():
                if spos > len(sub_parts):
                    continue
                raw_sub = sub_parts[spos - 1]
                if raw_sub:
                    sub_result[sfname] = _unescape(raw_sub, enc)
            if sub_result:
                result[fname] = sub_result
        else:
            result[fname] = _unescape(raw_comp, enc)

    return result or None


def _parse_field(raw: str, base_type: Any, is_list: bool, enc: EncodingChars) -> Any:
    if not raw:
        return None
    if is_list:
        parsed = [_parse_rep(r, base_type, enc) for r in raw.split(enc.repetition) if r]
        keep = [p for p in parsed if p is not None]
        return keep or None
    return _parse_rep(raw, base_type, enc)


def decode_er7_segment(
    seg_str: str,
    seg_cls: type[BaseModel],
    enc: EncodingChars = DEFAULT_ENCODING,
    *,
    strict: bool = True,
) -> BaseModel:
    """Decode a single ER7 segment string into a typed segment model.

    Parameters
    ----------
    seg_str : str
        A single ER7 segment string, e.g. ``"MSA|AA|MSG001"``.
    seg_cls : type[BaseModel]
        The segment model class to decode into.
    enc : EncodingChars, optional
        Delimiter characters to use for decoding. For delimiter-definition
        segments (``MSH``, ``FHS``, ``BHS``), the encoding characters are
        read from the segment string itself and override this value. Defaults
        to the standard HL7 encoding characters.
    strict : bool, optional
        If ``True`` (the default), raises ``pydantic.ValidationError`` when
        required fields are absent. If ``False``, missing required fields are
        filled with empty placeholder values and a ``UserWarning`` is emitted.

    Returns
    -------
    BaseModel
        A validated instance of ``seg_cls``.

    Raises
    ------
    pydantic.ValidationError
        If ``strict=True`` and required fields are missing, or if any field
        value fails format validation.

    Examples
    --------
    >>> from hl7types.hl7.v2_5_1.segments import MSA
    >>> from hl7types.codecs.er7.decoder import decode_er7_segment
    >>> seg = decode_er7_segment("MSA|AA|MSG001", MSA)
    >>> seg.msa_1
    'AA'
    """
    seg_name = seg_cls.__name__

    if seg_name in DELIM_DEF and len(seg_str) > 3:
        field_sep = seg_str[3]
        if field_sep != enc.field:
            rest = seg_str[4:]
            msh2_end = rest.find(field_sep)
            msh2 = rest[:msh2_end] if msh2_end != -1 else rest
            # Version unknown at this point; truncation support requires decode_er7 path
            base = EncodingChars.from_msh2(msh2) if msh2 else enc
            enc = EncodingChars(
                field=field_sep,
                component=base.component,
                repetition=base.repetition,
                escape=base.escape,
                subcomponent=base.subcomponent,
                truncation=base.truncation,
            )

    tokens = seg_str.split(enc.field)
    pm = _build_pos_map(seg_cls)
    data: dict[str, Any] = {}

    if seg_name in DELIM_DEF:
        if 1 in pm:
            data[pm[1][0]] = enc.field
        for i, token in enumerate(tokens[1:], start=2):
            if i not in pm:
                continue
            if i == 2:
                data[pm[2][0]] = token
                continue
            if not token:
                continue
            fname, base_type, is_list = pm[i]
            val = _parse_field(token, base_type, is_list, enc)
            if val is not None:
                data[fname] = val
    else:
        for i, token in enumerate(tokens[1:], start=1):
            if not token or i not in pm:
                continue
            fname, base_type, is_list = pm[i]
            val = _parse_field(token, base_type, is_list, enc)
            if val is not None:
                data[fname] = val

    if not strict:
        # Real-world messages routinely omit fields that the XSD marks as required.
        # Inject safe empty defaults so model_validate doesn't raise on missing keys:
        # composite fields get an empty dict (all their sub-fields are optional so
        # Pydantic constructs a zero-value instance), lists get [], scalars get "".
        skipped_fields: list[str] = []

        for _, (fname, base_type, is_list) in pm.items():
            if fname in data:
                continue
            if not seg_cls.model_fields[fname].is_required():
                continue

            skipped_fields.append(fname)

            if is_list:
                data[fname] = []
            elif _is_model(base_type):
                data[fname] = {}
            else:
                data[fname] = ""

        if skipped_fields:
            warnings.warn(
                (
                    f"Lenient ER7 decoding skipped missing required field(s) "
                    f"on segment {seg_name}: {', '.join(skipped_fields)}. "
                    "Placeholder values were injected because strict=False."
                ),
                UserWarning,
                stacklevel=2,
            )

    return seg_cls.model_validate(data)


def _decode_struct(
    segs: list[tuple[str, str]],
    idx: int,
    model_cls: type[BaseModel],
    enc: EncodingChars,
    *,
    strict: bool = True,
    registry: HL7Registry | None = None,
    _globally_reachable: frozenset[str] | None = None,
) -> tuple[int, BaseModel | None]:
    if is_segment_cls(model_cls, registry):
        if idx >= len(segs) or segs[idx][0] != model_cls.__name__:
            return idx, None
        return idx + 1, decode_er7_segment(segs[idx][1], model_cls, enc, strict=strict)

    hints = get_type_hints(model_cls)
    data: dict[str, Any] = {}

    # The reachable set is computed once at the message root and threaded down.
    # Using the root set (rather than the current sub-group's set) means segments
    # that belong to sibling groups are never mistakenly drained.
    if _globally_reachable is None:
        _globally_reachable = _reachable_segment_names(model_cls, registry)

    for fname in model_cls.model_fields:
        ann = hints.get(fname)
        if ann is None:
            continue
        base_type, is_list = _unwrap(ann)
        if not _is_model(base_type):
            continue

        # Drain segments whose names are not reachable anywhere in the message
        # structure. These are true unknowns (e.g. unregistered Z-segments).
        while idx < len(segs) and segs[idx][0] not in _globally_reachable:
            warnings.warn(
                f"Skipped unknown segment {segs[idx][0]!r} in {model_cls.__name__}.",
                UserWarning,
                stacklevel=2,
            )
            idx += 1

        seg_name = base_type.__name__
        resolved_type = (
            registry.get_segment(seg_name)
            if registry and is_segment_cls(base_type, registry)
            else None
        ) or base_type

        if is_list:
            items: list[Any] = []
            while idx < len(segs):
                # Drain unknowns between repetitions of a list field too.
                while idx < len(segs) and segs[idx][0] not in _globally_reachable:
                    warnings.warn(
                        f"Skipped unknown segment {segs[idx][0]!r} in {model_cls.__name__}.",
                        UserWarning,
                        stacklevel=2,
                    )
                    idx += 1
                if idx >= len(segs):
                    break
                new_idx, item = _decode_struct(
                    segs,
                    idx,
                    resolved_type,
                    enc,
                    strict=strict,
                    registry=registry,
                    _globally_reachable=_globally_reachable,
                )
                if item is None:
                    break
                items.append(item)
                idx = new_idx
            if items:
                data[fname] = items
        else:
            new_idx, item = _decode_struct(
                segs,
                idx,
                resolved_type,
                enc,
                strict=strict,
                registry=registry,
                _globally_reachable=_globally_reachable,
            )
            if item is not None:
                data[fname] = item
                idx = new_idx

    if not data:
        return idx, None

    if not strict:
        # A required segment or group may be absent from the wire (sender omitted it).
        # model_validate would raise on a missing required key, so we inject a
        # model_construct() placeholder, a bare instance with no field validation
        # for any required model-type field that wasn't found in the segment stream.
        # Scalar required fields on message/group models are not handled here because
        # those are owned by segments, which are covered in decode_er7_segment above.
        skipped_fields: list[str] = []

        for fname, fi in model_cls.model_fields.items():
            if fname in data or not fi.is_required():
                continue
            ann = hints.get(fname)
            if ann is None:
                continue
            base_type, is_list = _unwrap(ann)
            if not _is_model(base_type):
                continue

            skipped_fields.append(fname)
            data[fname] = [] if is_list else base_type.model_construct()

        if skipped_fields:
            warnings.warn(
                (
                    f"Lenient ER7 decoding skipped missing required segment/group "
                    f"field(s) on {model_cls.__name__}: {', '.join(skipped_fields)}. "
                    "Placeholder values were injected because strict=False."
                ),
                UserWarning,
                stacklevel=2,
            )

    return idx, model_cls.model_validate(data)


def _seg_name(seg_str: str, field_sep: str = "|") -> str:
    idx = seg_str.find(field_sep)
    return seg_str[:idx] if idx != -1 else seg_str


def _resolve_msg_cls(
    seg_strings: list[str],
    registry: HL7Registry | None = None,
) -> type[BaseModel]:
    msh_str = next(
        (s for s in seg_strings if s[:3] == "MSH"),
        None,
    )
    if not msh_str:
        raise ValueError("No MSH segment found, cannot auto-detect message type")

    if len(msh_str) < 4:
        raise ValueError(f"MSH segment too short to contain a field separator: {msh_str!r}")
    field_sep = msh_str[3]
    tokens = msh_str.split(field_sep)
    msh2 = tokens[1] if len(tokens) > 1 else ""
    msh12 = tokens[11] if len(tokens) > 11 else ""
    enc = EncodingChars.from_msh2(msh2, msh12 or None) if msh2 else DEFAULT_ENCODING
    comp_sep = enc.component

    msh9 = tokens[8] if len(tokens) > 8 else ""

    if not msh9:
        raise ValueError("MSH.9 is empty. Unable to auto-detect message type")
    if not msh12:
        raise ValueError("MSH.12 is empty. Unable to auto-detect HL7 version")

    parts = msh9.split(comp_sep)
    if len(parts) >= 3 and parts[2]:
        structure = parts[2]
    elif len(parts) >= 2 and parts[0] and parts[1]:
        structure = f"{parts[0]}_{parts[1]}"
    else:
        structure = parts[0]

    version = msh12.split(comp_sep)[0]

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


def _split_segments(wire: str, segment_separator: str) -> list[str]:
    if segment_separator in ("\r", "\n", "\r\n"):
        return [s for s in re.split(r"\r\n|\r|\n", wire) if s]
    return [s for s in wire.split(segment_separator) if s]


def decode_er7(
    wire: str,
    msg_cls: type[BaseModel] | None = None,
    segment_separator: str = "\r",
    *,
    strict: bool = True,
    registry: HL7Registry | None = None,
) -> BaseModel:
    """Decode an ER7 wire string into a typed message model.

    When ``msg_cls`` is not provided, the message class is resolved
    automatically from ``MSH.9`` (message type) and ``MSH.12`` (version) in
    the wire string. Encoding characters are read from the delimiter-definition
    segment in the wire and applied consistently throughout decoding.

    Parameters
    ----------
    wire : str
        A complete ER7-encoded message string with segments separated by
        ``segment_separator``.
    msg_cls : type[BaseModel], optional
        The message model class to decode into. If ``None``, the class is
        resolved dynamically from ``MSH.9`` and ``MSH.12``.
    segment_separator : str, optional
        Character used to split segments. Defaults to ``"\\r"``.
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
        A validated instance of the resolved or provided message class.

    Raises
    ------
    ValueError
        If the wire string is empty, no MSH segment is found, or the message
        type or version cannot be resolved to a known model class.
    pydantic.ValidationError
        If ``strict=True`` and required fields or segments are missing, or if
        any field value fails format validation.

    Examples
    --------
    >>> from hl7types import decode_er7
    >>> wire = "MSH|^~\\\\&|SEND||RECV||20260101||ACK|001|P|2.5.1\\rMSA|AA|001"
    >>> msg = decode_er7(wire)
    >>> msg.MSA.msa_1
    'AA'
    """
    seg_strings = _split_segments(wire, segment_separator)
    if not seg_strings:
        raise ValueError("Empty wire string")

    if msg_cls is None:
        msg_cls = _resolve_msg_cls(seg_strings, registry=registry)

    enc = DEFAULT_ENCODING
    for ss in seg_strings:
        if ss[:3] in DELIM_DEF and len(ss) > 3:
            field_sep = ss[3]
            tokens = ss.split(field_sep)
            msh2 = tokens[1] if len(tokens) > 1 else ""
            msh12 = tokens[11] if len(tokens) > 11 else ""
            base = EncodingChars.from_msh2(msh2, msh12 or None) if msh2 else DEFAULT_ENCODING
            enc = EncodingChars(
                field=field_sep,
                component=base.component,
                repetition=base.repetition,
                escape=base.escape,
                subcomponent=base.subcomponent,
                truncation=base.truncation,
            )
            break

    segs = [(_seg_name(ss, enc.field), ss) for ss in seg_strings]
    _, result = _decode_struct(segs, 0, msg_cls, enc, strict=strict, registry=registry)
    if result is None:
        raise ValueError(f"Could not decode wire string as {msg_cls.__name__}")
    return result
