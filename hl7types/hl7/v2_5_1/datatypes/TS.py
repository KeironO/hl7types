"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: TS
Type: Datatype
"""
from __future__ import annotations

import re

from typing import Optional
from pydantic import AliasChoices, ConfigDict, Field, ValidationInfo, field_validator
from hl7types.hl7 import HL7Model
from hl7types.hl7._validators import _apply_dt_fallback

_RE_DTM = re.compile(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?')


class TS(HL7Model):
    """Time stamp (S2.A.1.77).

    Attributes
    ----------
    ts_1 : str | None
        TS.1 (opt) - Time (DTM)

    ts_2 : str | None
        TS.2 (opt) - Degree of Precision (ID)
    """

    ts_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ts_1",
            "time",
            "TS.1",
        ),
        serialization_alias="TS.1",
        title="Time",
    )

    ts_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ts_2",
            "degree_of_precision",
            "TS.2",
        ),
        serialization_alias="TS.2",
        title="Degree of Precision",
    )

    @field_validator("ts_1", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        if _RE_DTM.fullmatch(v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    model_config = ConfigDict(populate_by_name=True)
