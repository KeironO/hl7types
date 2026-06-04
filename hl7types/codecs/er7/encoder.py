from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any, cast

from pydantic import BaseModel

DELIM_DEF = frozenset({"MSH", "FHS", "BHS"})
SEG_ALIAS_RE = re.compile(r"^[A-Z][A-Z0-9]{1,3}\.\d+$")


@dataclass(frozen=True)
class EncodingChars:
    field: str = "|"
    component: str = "^"
    repetition: str = "~"
    escape: str = "\\"
    subcomponent: str = "&"
    truncation: str = ""

    @classmethod
    def from_msh2(cls, msh2: str, hl7_version: str | None = None) -> EncodingChars:
        if len(msh2) not in (4, 5):
            raise ValueError(
                f"MSH.2 must be 4 or 5 encoding characters, got {len(msh2)!r}: {msh2!r}"
            )
        truncation = ""
        if len(msh2) == 5:
            v = hl7_version or ""
            try:
                major, minor = int(v.split(".")[0]), int(v.split(".")[1]) if "." in v else 0
            except (ValueError, IndexError):
                major, minor = 0, 0
            if (major, minor) < (2, 7):
                raise ValueError(
                    f"Truncation character in MSH.2 is only supported from HL7 v2.7 "
                    f"(got version {hl7_version!r})"
                )
            truncation = msh2[4]
        return cls(
            component=msh2[0],
            repetition=msh2[1],
            escape=msh2[2],
            subcomponent=msh2[3],
            truncation=truncation,
        )


DEFAULT_ENCODING = EncodingChars()


def _strip_trailing(s: str, delim: str) -> str:
    n = len(delim)
    while s.endswith(delim):
        s = s[:-n]
    return s


def _pos(key: str) -> int | None:
    dot = key.rfind(".")
    if dot == -1:
        return None
    suffix = key[dot + 1 :]
    return int(suffix) if suffix.isdigit() else None


def _pos_map(d: dict[str, Any]) -> dict[int, Any]:
    result: dict[int, Any] = {}
    for k, v in d.items():
        p = _pos(k)
        if p is not None:
            result[p] = v
    return result


def _escape(value: str, enc: EncodingChars) -> str:
    e = re.escape(enc.escape)
    # Split on existing escape sequences (\XXXX\) so they are preserved verbatim.
    # Even-indexed parts are literal text; odd-indexed parts are captured sequences.
    parts = re.split(f"({e}[^{e}]+{e})", value)
    out: list[str] = []
    for i, part in enumerate(parts):
        if i % 2 == 1:
            out.append(part)
        else:
            part = part.replace(enc.escape, f"{enc.escape}E{enc.escape}")
            part = part.replace(enc.field, f"{enc.escape}F{enc.escape}")
            part = part.replace(enc.component, f"{enc.escape}S{enc.escape}")
            part = part.replace(enc.repetition, f"{enc.escape}R{enc.escape}")
            part = part.replace(enc.subcomponent, f"{enc.escape}T{enc.escape}")
            if enc.truncation:
                part = part.replace(enc.truncation, f"{enc.escape}Z{enc.escape}")
            out.append(part)
    return "".join(out)


def _encode_subcomposite(d: dict[str, Any], enc: EncodingChars) -> str:
    pm = _pos_map(d)
    if not pm:
        return ""
    parts: list[str] = []
    for i in range(1, max(pm) + 1):
        val = pm.get(i)
        parts.append(_escape(val, enc) if isinstance(val, str) else "")
    return _strip_trailing(enc.subcomponent.join(parts), enc.subcomponent)


def _encode_composite(d: dict[str, Any], enc: EncodingChars, skip_escape: bool = False) -> str:
    pm = _pos_map(d)
    if not pm:
        return ""
    parts: list[str] = []
    for i in range(1, max(pm) + 1):
        val = pm.get(i)
        if val is None:
            parts.append("")
        elif isinstance(val, str):
            # Skip escaping for MSH-9 message type field
            parts.append(val if skip_escape else _escape(val, enc))
        elif isinstance(val, dict):
            parts.append(_encode_subcomposite(cast(dict[str, Any], val), enc))
        else:
            parts.append("")
    return _strip_trailing(enc.component.join(parts), enc.component)


def _encode_value(val: Any, enc: EncodingChars) -> str:
    if val is None:
        return ""
    if isinstance(val, str):
        return _escape(val, enc)
    if isinstance(val, list):
        reps = [_encode_value(item, enc) for item in cast(list[Any], val)]
        return _strip_trailing(enc.repetition.join(reps), enc.repetition)
    if isinstance(val, dict):
        return _encode_composite(cast(dict[str, Any], val), enc)
    return _escape(str(val), enc)


def is_segment(model: BaseModel) -> bool:
    for fi in type(model).model_fields.values():
        alias = fi.serialization_alias
        if isinstance(alias, str) and SEG_ALIAS_RE.match(alias):
            return True
    return False


def _collect_segments(obj: BaseModel) -> list[BaseModel]:
    segs: list[BaseModel] = []
    for fname in type(obj).model_fields:
        value = getattr(obj, fname)
        if value is None:
            continue
        items: list[Any] = cast(list[Any], value) if isinstance(value, list) else [value]
        for item in items:
            if not isinstance(item, BaseModel):
                continue
            if is_segment(item):
                segs.append(item)
            else:
                segs.extend(_collect_segments(item))
    return segs


def encode_er7_segment(seg: BaseModel, enc: EncodingChars = DEFAULT_ENCODING) -> str:
    """Encode a single segment model to an ER7 segment string.

    Parameters
    ----------
    seg : BaseModel
        The segment model instance to encode.
    enc : EncodingChars, optional
        Delimiter characters to use. Defaults to the standard HL7 encoding
        characters (``|``, ``^``, ``~``, ``\\``, ``&``).

    Returns
    -------
    str
        A single ER7 segment string with no trailing separator, e.g.
        ``"MSA|AA|MSG001"``.

    Examples
    --------
    >>> from hl7types.hl7.v2_5_1.segments import MSA
    >>> from hl7types.codecs.er7.encoder import encode_er7_segment
    >>> encode_er7_segment(MSA(msa_1="AA", msa_2="MSG001"))
    'MSA|AA|MSG001'
    """
    seg_name = type(seg).__name__
    d = seg.model_dump(by_alias=True)
    pm = _pos_map(d)
    if not pm:
        return seg_name

    max_pos = max(pm)

    if seg_name in DELIM_DEF:
        stored_msh2 = str(pm.get(2, "") or "")
        if not stored_msh2:
            stored_msh2 = f"{enc.component}{enc.repetition}{enc.escape}{enc.subcomponent}"
            if enc.truncation:
                stored_msh2 += enc.truncation
        parts: list[str] = [stored_msh2]
        for i in range(3, max_pos + 1):
            val = pm.get(i)
            # MSH-9 contains composite separators literally; never escape them
            if seg_name == "MSH" and i == 9:
                if isinstance(val, dict):
                    parts.append(_encode_composite(cast(dict[str, Any], val), enc))
                elif isinstance(val, str):
                    parts.append(val)
                else:
                    parts.append(_encode_value(val, enc) if val is not None else "")
            else:
                parts.append(_encode_value(val, enc) if val is not None else "")
    else:
        parts: list[str] = []
        for i in range(1, max_pos + 1):
            val = pm.get(i)
            parts.append(_encode_value(val, enc) if val is not None else "")

    result = seg_name + enc.field + enc.field.join(parts)
    return _strip_trailing(result, enc.field)


def encode_er7(model: BaseModel, segment_separator: str = "\r") -> str:
    """Encode a message or segment model to an ER7 wire string.

    Encoding characters are read from the delimiter-definition segment
    (``MSH``, ``FHS``, or ``BHS``) in the model if present, falling back to
    the standard HL7 defaults.

    Parameters
    ----------
    model : BaseModel
        The message, group, or segment model instance to encode.
    segment_separator : str, optional
        Character used to join segments. The HL7 v2 specification mandates a
        carriage return (``\\r``, ASCII 0x0D). Defaults to ``"\\r"``.

    Returns
    -------
    str
        ER7-encoded wire string with segments joined by ``segment_separator``.
        Returns an empty string if the model contains no encodable segments.

    Examples
    --------
    >>> from hl7types.hl7.v2_5_1.segments import MSA
    >>> from hl7types.codecs.er7.encoder import encode_er7
    >>> encode_er7(MSA(msa_1="AA", msa_2="MSG001"))
    'MSA|AA|MSG001'
    """
    if is_segment(model):
        return encode_er7_segment(model)

    segments = _collect_segments(model)
    if not segments:
        return ""

    enc = DEFAULT_ENCODING
    for seg in segments:
        if type(seg).__name__ in DELIM_DEF:
            d = seg.model_dump(by_alias=True)
            msh1 = d.get("MSH.1") or d.get("FHS.1") or d.get("BHS.1")
            msh2 = d.get("MSH.2") or d.get("FHS.2") or d.get("BHS.2")
            msh12 = d.get("MSH.12") or d.get("FHS.12") or d.get("BHS.12")
            if isinstance(msh12, str):
                hl7_version = msh12
            elif isinstance(msh12, dict):
                # VID composite , first component is the version string
                hl7_version = next((v for v in msh12.values() if isinstance(v, str)), None)  # type: ignore
            else:
                hl7_version = None
            field_sep = msh1 if isinstance(msh1, str) and msh1 else DEFAULT_ENCODING.field
            base = EncodingChars.from_msh2(msh2, hl7_version) if msh2 else DEFAULT_ENCODING
            enc = EncodingChars(
                field=field_sep,
                component=base.component,
                repetition=base.repetition,
                escape=base.escape,
                subcomponent=base.subcomponent,
                truncation=base.truncation,
            )
            break

    return segment_separator.join(encode_er7_segment(seg, enc) for seg in segments)
