"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: CM2
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CE import CE


class CM2(BaseModel):
    """HL7 v2 CM2 segment."""

    cm2_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm2_1",
            "set_id_cm2",
            "CM2.1",
        ),
        serialization_alias="CM2.1",
        title="Set ID - CM2",
        description="Item #1024",
    )

    cm2_2: CE = Field(
        default=...,
        validation_alias=AliasChoices(
            "cm2_2",
            "scheduled_time_point",
            "CM2.2",
        ),
        serialization_alias="CM2.2",
        title="Scheduled Time Point",
        description="Item #1025",
    )

    cm2_3: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm2_3",
            "description_of_time_point",
            "CM2.3",
        ),
        serialization_alias="CM2.3",
        title="Description of Time Point",
        description="Item #1026",
    )

    cm2_4: list[CE] = Field(
        default=...,
        validation_alias=AliasChoices(
            "cm2_4",
            "events_scheduled_this_time_point",
            "CM2.4",
        ),
        serialization_alias="CM2.4",
        title="Events Scheduled This Time Point",
        description="Item #1027",
    )

    model_config = {"populate_by_name": True}
