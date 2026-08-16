from __future__ import annotations

import re
from dataclasses import dataclass

DELIM_DEF = frozenset({"MSH", "FHS", "BHS"})


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


def split_segments(wire: str, segment_separator: str) -> list[str]:
    if segment_separator in ("\r", "\n", "\r\n"):
        return [segment for segment in re.split(r"\r\n|\r|\n", wire) if segment]
    return [segment for segment in wire.split(segment_separator) if segment]


def encoding_from_segment(
    segment: str,
    *,
    fallback: EncodingChars = DEFAULT_ENCODING,
    hl7_version: str | None = None,
    strict: bool = True,
) -> EncodingChars | None:
    if segment[:3] not in DELIM_DEF or len(segment) < 4:
        return None

    field = segment[3]
    msh2 = segment[4:].split(field, 1)[0]
    if strict:
        base = EncodingChars.from_msh2(msh2, hl7_version) if msh2 else fallback
    else:
        base = EncodingChars(
            component=msh2[0] if len(msh2) > 0 else fallback.component,
            repetition=msh2[1] if len(msh2) > 1 else fallback.repetition,
            escape=msh2[2] if len(msh2) > 2 else fallback.escape,
            subcomponent=msh2[3] if len(msh2) > 3 else fallback.subcomponent,
            truncation=msh2[4] if len(msh2) > 4 else "",
        )
    return EncodingChars(
        field=field,
        component=base.component,
        repetition=base.repetition,
        escape=base.escape,
        subcomponent=base.subcomponent,
        truncation=base.truncation,
    )
