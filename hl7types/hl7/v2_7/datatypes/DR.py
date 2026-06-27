"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: DR
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field, field_validator, ValidationInfo
from hl7types.hl7 import HL7Model
from hl7types.hl7._validators import _apply_dt_fallback


class DR(HL7Model):
    """HL7 v2 DR data type.

    Attributes
    ----------
    dr_1 : str | None
        DR.1 (opt) - Range Start Date/Time (DTM)

    dr_2 : str | None
        DR.2 (opt) - Range End Date/Time (DTM)
    """

    dr_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dr_1",
            "range_start_date_time",
            "DR.1",
        ),
        serialization_alias="DR.1",
        title="Range Start Date/Time",
    )

    dr_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dr_2",
            "range_end_date_time",
            "DR.2",
        ),
        serialization_alias="DR.2",
        title="Range End Date/Time",
    )

    @field_validator("dr_1", "dr_2", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        import re
        if re.fullmatch(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?', v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    model_config = {"populate_by_name": True}
