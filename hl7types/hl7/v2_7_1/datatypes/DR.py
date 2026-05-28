"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: DR
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field


class DR(BaseModel):
    """HL7 v2 DR data type."""

    dr_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "dr_1",
            "range_start_date_time",
            "DR.1",
        ),
        serialization_alias="DR.1",
        title="Range Start Date/Time",
    )

    dr_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "dr_2",
            "range_end_date_time",
            "DR.2",
        ),
        serialization_alias="DR.2",
        title="Range End Date/Time",
    )

    model_config = {"populate_by_name": True}
