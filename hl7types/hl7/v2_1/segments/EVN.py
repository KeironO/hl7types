"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: EVN
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field


class EVN(BaseModel):
    """HL7 v2 EVN segment."""

    evn_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "evn_1",
            "event_type_code",
            "EVN.1",
        ),
        serialization_alias="EVN.1",
        title="EVENT TYPE CODE",
        description="Item #29 | Table HL70003",
    )

    evn_2: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "evn_2",
            "date_time_of_event",
            "EVN.2",
        ),
        serialization_alias="EVN.2",
        title="DATE/TIME OF EVENT",
        description="Item #30",
    )

    evn_3: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "evn_3",
            "date_time_planned_event",
            "EVN.3",
        ),
        serialization_alias="EVN.3",
        title="DATE/TIME PLANNED EVENT",
        description="Item #32",
    )

    evn_4: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "evn_4",
            "event_reason_code",
            "EVN.4",
        ),
        serialization_alias="EVN.4",
        title="EVENT REASON CODE",
        description="Item #369 | Table HL70062",
    )

    model_config = {"populate_by_name": True}
