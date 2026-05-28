from __future__ import annotations

import importlib
import re
import typing
from functools import lru_cache
from typing import Any, get_type_hints

from pydantic import BaseModel

from hl7types.codecs.er7.encoder import (
    _DELIM_DEF,
    _SEG_ALIAS_RE,
    DEFAULT_ENCODING,
    EncodingChars,
)

_UNESCAPE_MAP: dict[str, str] = {
    "F": "|",
    "S": "^",
    "T": "&",
    "R": "~",
    "E": "\\",
}


def _unescape(value: str, enc: EncodingChars) -> str:
    e = re.escape(enc.escape)
    return re.sub(
        f"{e}([FSTRET]){e}",
        lambda m: _UNESCAPE_MAP.get(m.group(1), m.group(0)),
        value,
    )


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


def _is_segment_cls(cls: Any) -> bool:
    if not _is_model(cls):
        return False
    for fi in cls.model_fields.values():
        alias = fi.serialization_alias
        if isinstance(alias, str) and _SEG_ALIAS_RE.match(alias):
            return True
    return False


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
        alias = field_type.model_fields[fname].serialization_alias
        if _is_model(sub_type):
            sub_pm = _build_pos_map(sub_type)
            sub_parts = raw_comp.split(enc.subcomponent)
            sub_result: dict[str, Any] = {}
            for spos, (sfname, _, _) in sub_pm.items():
                if spos > len(sub_parts):
                    continue
                raw_sub = sub_parts[spos - 1]
                if raw_sub:
                    salias = sub_type.model_fields[sfname].serialization_alias
                    sub_result[salias] = _unescape(raw_sub, enc)
            if sub_result:
                result[alias] = sub_result
        else:
            result[alias] = _unescape(raw_comp, enc)

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
) -> BaseModel:
    seg_name = seg_cls.__name__

    if seg_name in _DELIM_DEF and len(seg_str) > 3:
        field_sep = seg_str[3]
        if field_sep != enc.field:
            rest = seg_str[4:]
            msh2_end = rest.find(field_sep)
            msh2 = rest[:msh2_end] if msh2_end != -1 else rest
            base = EncodingChars.from_msh2(msh2) if msh2 else enc
            enc = EncodingChars(
                field=field_sep,
                component=base.component,
                repetition=base.repetition,
                escape=base.escape,
                subcomponent=base.subcomponent,
            )

    tokens = seg_str.split(enc.field)
    pm = _build_pos_map(seg_cls)
    data: dict[str, Any] = {}

    if seg_name in _DELIM_DEF:
        if 1 in pm:
            alias1 = seg_cls.model_fields[pm[1][0]].serialization_alias
            assert alias1 is not None
            data[alias1] = enc.field
        for i, token in enumerate(tokens[1:], start=2):
            if i not in pm:
                continue
            if i == 2:
                alias2 = seg_cls.model_fields[pm[2][0]].serialization_alias
                assert alias2 is not None
                data[alias2] = token
                continue
            if not token:
                continue
            fname, base_type, is_list = pm[i]
            alias = seg_cls.model_fields[fname].serialization_alias
            assert alias is not None
            val = _parse_field(token, base_type, is_list, enc)
            if val is not None:
                data[alias] = val
    else:
        for i, token in enumerate(tokens[1:], start=1):
            if not token or i not in pm:
                continue
            fname, base_type, is_list = pm[i]
            alias = seg_cls.model_fields[fname].serialization_alias
            assert alias is not None
            val = _parse_field(token, base_type, is_list, enc)
            if val is not None:
                data[alias] = val

    # Real-world messages routinely omit fields that the XSD marks as required.
    # Inject safe empty defaults so model_validate doesn't raise on missing keys:
    # composite fields get an empty dict (all their sub-fields are optional so
    # Pydantic constructs a zero-value instance), lists get [], scalars get "".
    for pos, (fname, base_type, is_list) in pm.items():
        fi = seg_cls.model_fields[fname]
        fi_alias = fi.serialization_alias
        assert fi_alias is not None
        if fi_alias in data:
            continue
        if not fi.is_required():
            continue
        if is_list:
            data[fi_alias] = []
        elif _is_model(base_type):
            data[fi_alias] = {}
        else:
            data[fi_alias] = ""

    return seg_cls.model_validate(data)


def _decode_struct(
    segs: list[tuple[str, str]],
    idx: int,
    model_cls: type[BaseModel],
    enc: EncodingChars,
) -> tuple[int, BaseModel | None]:
    if _is_segment_cls(model_cls):
        if idx >= len(segs) or segs[idx][0] != model_cls.__name__:
            return idx, None
        return idx + 1, decode_er7_segment(segs[idx][1], model_cls, enc)

    hints = get_type_hints(model_cls)
    data: dict[str, Any] = {}

    for fname in model_cls.model_fields:
        ann = hints.get(fname)
        if ann is None:
            continue
        base_type, is_list = _unwrap(ann)
        if not _is_model(base_type):
            continue

        if is_list:
            items: list[Any] = []
            while idx < len(segs):
                new_idx, item = _decode_struct(segs, idx, base_type, enc)
                if item is None:
                    break
                items.append(item)
                idx = new_idx
            if items:
                data[fname] = items
        else:
            new_idx, item = _decode_struct(segs, idx, base_type, enc)
            if item is not None:
                data[fname] = item
                idx = new_idx

    if not data:
        return idx, None

    # A required segment or group may be absent from the wire (sender omitted it).
    # model_validate would raise on a missing required key, so we inject a
    # model_construct() placeholder — a bare instance with no field validation —
    # for any required model-type field that wasn't found in the segment stream.
    # Scalar required fields on message/group models are not handled here because
    # those are owned by segments, which are covered in decode_er7_segment above.
    for fname, fi in model_cls.model_fields.items():
        if fname in data or not fi.is_required():
            continue
        ann = hints.get(fname)
        if ann is None:
            continue
        base_type, is_list = _unwrap(ann)
        if not _is_model(base_type):
            continue
        data[fname] = [] if is_list else base_type.model_construct()

    return idx, model_cls.model_validate(data)


def _version_to_module(version: str) -> str:
    return "v" + version.replace(".", "_")


def _resolve_msg_cls(wire: str, segment_separator: str) -> type[BaseModel]:
    msh_str = next(
        (s for s in wire.split(segment_separator) if s[:3] == "MSH"),
        None,
    )
    if not msh_str:
        raise ValueError("No MSH segment found — cannot auto-detect message type")

    if len(msh_str) < 4:
        raise ValueError(f"MSH segment too short to contain a field separator: {msh_str!r}")
    field_sep = msh_str[3]
    tokens = msh_str.split(field_sep)
    msh2 = tokens[1] if len(tokens) > 1 else ""
    enc = EncodingChars.from_msh2(msh2) if msh2 else DEFAULT_ENCODING
    comp_sep = enc.component

    msh9 = tokens[8] if len(tokens) > 8 else ""
    msh12 = tokens[11] if len(tokens) > 11 else ""

    if not msh9:
        raise ValueError("MSH.9 is empty — cannot auto-detect message type")
    if not msh12:
        raise ValueError("MSH.12 is empty — cannot auto-detect HL7 version")

    parts = msh9.split(comp_sep)
    if len(parts) >= 3 and parts[2]:
        structure = parts[2]
    elif len(parts) >= 2 and parts[0] and parts[1]:
        structure = f"{parts[0]}_{parts[1]}"
    else:
        structure = parts[0]

    mod_name = _version_to_module(msh12.split(comp_sep)[0])
    module = importlib.import_module(f"hl7types.hl7.{mod_name}.messages.{structure}")
    return getattr(module, structure)


def decode_er7(
    wire: str,
    msg_cls: type[BaseModel] | None = None,
    segment_separator: str = "\r",
) -> BaseModel:
    seg_strings = [s for s in re.split(r"\r\n|\r|\n", wire) if s]
    if not seg_strings:
        raise ValueError("Empty wire string")

    if msg_cls is None:
        msg_cls = _resolve_msg_cls(wire, segment_separator)

    enc = DEFAULT_ENCODING
    for ss in seg_strings:
        if ss[:3] in _DELIM_DEF and len(ss) > 3:
            field_sep = ss[3]
            rest = ss[4:]
            msh2_end = rest.find(field_sep)
            msh2 = rest[:msh2_end] if msh2_end != -1 else rest
            base = EncodingChars.from_msh2(msh2) if msh2 else DEFAULT_ENCODING
            enc = EncodingChars(
                field=field_sep,
                component=base.component,
                repetition=base.repetition,
                escape=base.escape,
                subcomponent=base.subcomponent,
            )
            break

    segs = [(ss[:3], ss) for ss in seg_strings]
    _, result = _decode_struct(segs, 0, msg_cls, enc)
    if result is None:
        raise ValueError(f"Could not decode wire string as {msg_cls.__name__}")
    return result
