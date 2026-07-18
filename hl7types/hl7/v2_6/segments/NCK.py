"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: NCK
Type: Segment
"""
from __future__ import annotations

import re

from pydantic import AliasChoices, ConfigDict, Field, ValidationInfo, field_validator
from hl7types.hl7 import HL7Model
from hl7types.hl7._validators import _apply_dt_fallback

_RE_DTM = re.compile(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?')


class NCK(HL7Model):
    """System Clock (S14.4.1).

    Attributes
    ----------
    nck_1 : str
        NCK.1 - System Date/Time (DTM) R S14.4.1.1
    """

    nck_1: str = Field(
        validation_alias=AliasChoices(
            "nck_1",
            "system_date_time",
            "NCK.1",
        ),
        serialization_alias="NCK.1",
        title="System Date/Time",
        description="R | Item #01172 | LEN:24",
    )

    @field_validator("nck_1", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        if _RE_DTM.fullmatch(v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    model_config = ConfigDict(populate_by_name=True)
