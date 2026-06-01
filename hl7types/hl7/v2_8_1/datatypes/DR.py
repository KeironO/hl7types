"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: DR
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model
from pydantic import field_validator


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
    def _validate_dtm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?', v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 datetime")
        return v

    model_config = {"populate_by_name": True}
