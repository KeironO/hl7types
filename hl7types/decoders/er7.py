from __future__ import annotations

import importlib
import re
import typing
from functools import lru_cache
from typing import Any, get_type_hints

from pydantic import BaseModel

from hl7types.encoders.er7 import DEFAULT_ENCODING, EncodingChars, _SEG_ALIAS_RE

# Unescape

_UNESCAPE_MAP: dict[str, str] = {
    "F": "|",
    "S": "^",
    "T": "&",
    "R": "~",
    "E": "\\",
}

_DELIM_DEF = frozenset({"MSH", "FHS", "BHS"})


def _unescape(value: str, enc: EncodingChars) -> str:
    e = re.escape(enc.escape)
    return re.sub(
        f"{e}([FSTRET]){e}",
        lambda m: _UNESCAPE_MAP.get(m.group(1), m.group(0)),
        value,
    )


# Type introspection helpers

def _unwrap(annotation: Any) -> tuple[Any, bool]:
    """Unwrap Optional[List[X]] / Optional[X] / List[X] / X → (inner_type, is_list)."""
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
    """True if cls is a segment-level model (fields carry serialization_alias like MSH.1)."""
    if not _is_model(cls):
        return False
    for fi in cls.model_fields.values():
        alias = fi.serialization_alias
        if isinstance(alias, str) and _SEG_ALIAS_RE.match(alias):
            return True
    return False


# Position map: {field_position: (field_name, base_type, is_list)}

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


# Value parsing: field to repetition to component to subcaomponent

def _parse_rep(raw: str, field_type: Any, enc: EncodingChars) -> Any:
    """Parse one repetition of a field value into a str or a keyed dict."""
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
            # subcoomponent level: split by & and recurse one more time (str only)
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


# Segment decoding

def decode_segment(
    seg_str: str,
    seg_cls: type[BaseModel],
    enc: EncodingChars = DEFAULT_ENCODING,
) -> BaseModel:
    """Decode a single pipe-encoded segment string into a typed Pydantic model.

    This is a pretty good first go at it, but it struggles with larger segments."""
    seg_name = seg_cls.__name__

    # For delimiter-defining segments, always derive the field sep from position 3
    # (the character right after the 3-char name), overriding whatever enc was passed.
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
        # tokens[0] = "MSH"; tokens[1] = MSH.2 (encoding chars literal); tokens[2+] = MSH.3+
        if 1 in pm:
            data[seg_cls.model_fields[pm[1][0]].serialization_alias] = enc.field
        for i, token in enumerate(tokens[1:], start=2):
            if i not in pm:
                continue
            if i == 2:
                # MSH.2 is written literally — never split/unescaped
                data[seg_cls.model_fields[pm[2][0]].serialization_alias] = token
                continue
            if not token:
                continue
            fname, base_type, is_list = pm[i]
            alias = seg_cls.model_fields[fname].serialization_alias
            val = _parse_field(token, base_type, is_list, enc)
            if val is not None:
                data[alias] = val
    else:
        # tokens[0] = segment name; tokens[n] = field n (1-indexed)
        for i, token in enumerate(tokens[1:], start=1):
            if not token or i not in pm:
                continue
            fname, base_type, is_list = pm[i]
            alias = seg_cls.model_fields[fname].serialization_alias
            val = _parse_field(token, base_type, is_list, enc)
            if val is not None:
                data[alias] = val

    return seg_cls.model_validate(data)

# Message decoding (greedy tree-walk)

def _decode_struct(
    segs: list[tuple[str, str]],
    idx: int,
    model_cls: type[BaseModel],
    enc: EncodingChars,
) -> tuple[int, BaseModel | None]:
    """Greedily decode model_cls starting at segs[idx].

    We need to take a look at whether GTW Is the way we want to walk

    Returns (new_idx, instance) on success, or (original_idx, None) if no match.
    """
    if _is_segment_cls(model_cls):
        if idx >= len(segs) or segs[idx][0] != model_cls.__name__:
            return idx, None
        return idx + 1, decode_segment(segs[idx][1], model_cls, enc)

    # Group or message: walk fields in declaration order
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
    return idx, model_cls.model_validate(data)


def _version_to_module(version: str) -> str:
    """'2.5.1' to 'v2_5_1'."""
    return "v" + version.replace(".", "_")


def _resolve_msg_cls(wire: str, segment_separator: str) -> type[BaseModel]:
    """Infer the message class from MSH.9 (structure) and MSH.12 (version)."""
    msh_str = next(
        (s for s in wire.split(segment_separator) if s[:3] == "MSH"),
        None,
    )
    if not msh_str:
        raise ValueError("No MSH segment found — cannot auto-detect message type")

    field_sep = msh_str[3]
    tokens = msh_str.split(field_sep)
    # tokens[1] = MSH.2 (encoding chars), tokens[8] = MSH.9, tokens[11] = MSH.12
    comp_sep = tokens[1][0] if len(tokens) > 1 and tokens[1] else "^"

    msh9 = tokens[8] if len(tokens) > 8 else ""
    msh12 = tokens[11] if len(tokens) > 11 else ""

    if not msh9:
        raise ValueError("MSH.9 is empty — cannot auto-detect message type")
    if not msh12:
        raise ValueError("MSH.12 is empty — cannot auto-detect HL7 version")

    parts = msh9.split(comp_sep)
    # MSH.9.3 is the message structure; fall back to MSH.9.1_MSH.9.2
    if len(parts) >= 3 and parts[2]:
        structure = parts[2]
    elif len(parts) >= 2 and parts[0] and parts[1]:
        structure = f"{parts[0]}_{parts[1]}"
    else:
        structure = parts[0]

    mod_name = _version_to_module(msh12)
    module = importlib.import_module(f"hl7types.{mod_name}.messages.{structure}")
    return getattr(module, structure)


def decode(
    wire: str,
    msg_cls: type[BaseModel] | None = None,
    segment_separator: str = "\r",
) -> BaseModel:
    """Decode a pipe-encoded HL7 message string into a typed Pydantic model.

    If msg_cls is omitted the class is resolved automatically from MSH.9
    (message structure) and MSH.12 (version).
    """
    seg_strings = [s for s in wire.split(segment_separator) if s]
    if not seg_strings:
        raise ValueError("Empty wire string")

    if msg_cls is None:
        msg_cls = _resolve_msg_cls(wire, segment_separator)

    # Derive encoding chars from first delimiter-defining segment.
    # MSH.1 is always seg_str[3] (the char right after the 3-char segment name).
    # MSH.2 (encoding chars) follows immediately: seg_str[4:8] before the next MSH.1.
    enc = DEFAULT_ENCODING
    for ss in seg_strings:
        if ss[:3] in _DELIM_DEF and len(ss) > 3:
            field_sep = ss[3]
            # MSH.2 is the run of chars between positions 4 and the next field_sep
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
