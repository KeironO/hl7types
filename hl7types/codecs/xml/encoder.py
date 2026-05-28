from __future__ import annotations

import typing
from typing import Any, get_type_hints
from xml.etree import ElementTree as ET

from pydantic import BaseModel

from hl7types.codecs.er7.encoder import _SEG_ALIAS_RE

_HL7_XML_NS = "urn:hl7-org:v2xml"


def _is_model(cls: Any) -> bool:
    try:
        return isinstance(cls, type) and issubclass(cls, BaseModel)
    except TypeError:
        return False


def _is_segment_cls(model: BaseModel) -> bool:
    for fi in type(model).model_fields.values():
        alias = fi.serialization_alias
        if isinstance(alias, str) and _SEG_ALIAS_RE.match(alias):
            return True
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


def _field_pos(key: str) -> int:
    dot = key.rfind(".")
    if dot == -1:
        return 0
    suffix = key[dot + 1 :]
    return int(suffix) if suffix.isdigit() else 0


def _dict_to_children(d: dict[str, Any], parent: ET.Element) -> None:
    for key, val in sorted(d.items(), key=lambda kv: _field_pos(kv[0])):
        if isinstance(val, list):
            for item in val:
                child = ET.SubElement(parent, key)
                if isinstance(item, dict):
                    _dict_to_children(item, child)
                elif item is not None:
                    child.text = str(item)
        elif isinstance(val, dict):
            child = ET.SubElement(parent, key)
            _dict_to_children(val, child)
        else:
            child = ET.SubElement(parent, key)
            if val is not None:
                child.text = str(val)


def _group_xml_tag(cls: type) -> str:
    """ADT_A01_PROCEDURE to ADT_A01.PROCEDURE (last underscore becomes a dot)."""
    name = cls.__name__
    idx = name.rfind("_")
    return f"{name[:idx]}.{name[idx + 1 :]}" if idx != -1 else name


def _append_model(model: BaseModel, parent: ET.Element) -> None:
    cls = type(model)
    if _is_segment_cls(model):
        child = ET.SubElement(parent, cls.__name__)
        d = model.model_dump(by_alias=True, exclude_none=True)
        _dict_to_children(d, child)
    else:
        child = ET.SubElement(parent, _group_xml_tag(cls))
        _fill_composite(model, child)


def _fill_composite(model: BaseModel, elem: ET.Element) -> None:
    hints = get_type_hints(type(model))
    for fname in type(model).model_fields:
        value = getattr(model, fname)
        if value is None:
            continue
        ann = hints.get(fname)
        if ann is None:
            continue
        base_type, is_list = _unwrap(ann)
        if not _is_model(base_type):
            continue
        if is_list:
            for item in value:
                _append_model(item, elem)
        else:
            _append_model(value, elem)


def encode_xml(
    model: BaseModel,
    *,
    pretty: bool = True,
    namespace: str = _HL7_XML_NS,
) -> str:
    """Encode a message (or single segment) to HL7 v2 XML format."""
    cls = type(model)
    root = ET.Element(cls.__name__)
    root.set("xmlns", namespace)

    if _is_segment_cls(model):
        d = model.model_dump(by_alias=True, exclude_none=True)
        _dict_to_children(d, root)
    else:
        _fill_composite(model, root)

    declaration = '<?xml version="1.0" encoding="UTF-8"?>'
    if pretty:
        ET.indent(root, space="    ")
    return declaration + ET.tostring(root, encoding="unicode")
