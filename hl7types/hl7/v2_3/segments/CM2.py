"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: CM2
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CE import CE


class CM2(BaseModel):
    """HL7 v2 CM2 segment.

    Attributes
    ----------
    cm2_1 : str | None
        CM2.1 (opt) - CM2 - Set ID (SI)

    cm2_2 : CE
        CM2.2 (req) - Scheduled Time Point (CE)

    cm2_3 : str | None
        CM2.3 (opt) - Description of Time Point (ST)

    cm2_4 : list[CE]
        CM2.4 (req, rep) - Events Scheduled This Time Point (CE)
    """

    cm2_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm2_1",
            "cm2_set_id",
            "CM2.1",
        ),
        serialization_alias="CM2.1",
        title="CM2 - Set ID",
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

    cm2_3: Optional[str] = Field(
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

    cm2_4: List[CE] = Field(
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
