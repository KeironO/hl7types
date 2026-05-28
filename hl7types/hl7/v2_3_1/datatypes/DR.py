"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: DR
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from .TS import TS


class DR(BaseModel):
    """HL7 v2 DR data type."""

    dr_1: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dr_1",
            "range_start_date_time",
            "DR.1",
        ),
        serialization_alias="DR.1",
        title="range start date/time",
    )

    dr_2: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "dr_2",
            "range_end_date_time",
            "DR.2",
        ),
        serialization_alias="DR.2",
        title="range end date/time",
    )

    model_config = {"populate_by_name": True}
