"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: EVN
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.HD import HD
from ..datatypes.XCN import XCN


class EVN(BaseModel):
    """HL7 v2 EVN segment."""

    evn_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "evn_1",
            "event_type_code",
            "EVN.1",
        ),
        serialization_alias="EVN.1",
        title="Event Type Code",
        description="Item #99 | Table HL70003",
    )

    evn_2: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "evn_2",
            "recorded_date_time",
            "EVN.2",
        ),
        serialization_alias="EVN.2",
        title="Recorded Date/Time",
        description="Item #100",
    )

    evn_3: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "evn_3",
            "date_time_planned_event",
            "EVN.3",
        ),
        serialization_alias="EVN.3",
        title="Date/Time Planned Event",
        description="Item #101",
    )

    evn_4: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "evn_4",
            "event_reason_code",
            "EVN.4",
        ),
        serialization_alias="EVN.4",
        title="Event Reason Code",
        description="Item #102 | Table HL70062",
    )

    evn_5: list[XCN] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "evn_5",
            "operator_id",
            "EVN.5",
        ),
        serialization_alias="EVN.5",
        title="Operator ID",
        description="Item #103 | Table HL70188",
    )

    evn_6: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "evn_6",
            "event_occurred",
            "EVN.6",
        ),
        serialization_alias="EVN.6",
        title="Event Occurred",
        description="Item #1278",
    )

    evn_7: HD | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "evn_7",
            "event_facility",
            "EVN.7",
        ),
        serialization_alias="EVN.7",
        title="Event Facility",
        description="Item #1534",
    )

    model_config = {"populate_by_name": True}
