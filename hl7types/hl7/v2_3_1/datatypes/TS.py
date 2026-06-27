"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: TS
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field, field_validator, ValidationInfo
from hl7types.hl7 import HL7Model
from hl7types.hl7._validators import _apply_dt_fallback


class TS(HL7Model):
    """HL7 v2 TS data type.

    Attributes
    ----------
    ts_1 : str | None
        TS.1 (opt) - time of an event (ST)

    ts_2 : str | None
        TS.2 (opt) - degree of precision (ST)
    """

    ts_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ts_1",
            "time_of_an_event",
            "TS.1",
        ),
        serialization_alias="TS.1",
        title="time of an event",
    )

    ts_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ts_2",
            "degree_of_precision",
            "TS.2",
        ),
        serialization_alias="TS.2",
        title="degree of precision",
    )

    @field_validator("ts_1", mode='before')
    @classmethod
    def _validate_ts_pre25(cls, v: str, info: ValidationInfo) -> str:
        import re
        if re.fullmatch(r'(\d{4}([01]\d(\d{2}([012]\d[0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?([+\-]\d{4})?', v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dt_parser")), datatype="DT", field_path="TS.1")

    model_config = {"populate_by_name": True}
