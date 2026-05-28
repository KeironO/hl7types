"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: LA1
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from .AD import AD
from .HD import HD


class LA1(BaseModel):
    """HL7 v2 LA1 data type."""

    la1_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "la1_1",
            "point_of_care_is",
            "LA1.1",
        ),
        serialization_alias="LA1.1",
        title="point of care (IS)",
    )

    la1_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "la1_2",
            "room",
            "LA1.2",
        ),
        serialization_alias="LA1.2",
        title="room",
    )

    la1_3: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "la1_3",
            "bed",
            "LA1.3",
        ),
        serialization_alias="LA1.3",
        title="bed",
    )

    la1_4: HD | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "la1_4",
            "facility_hd",
            "LA1.4",
        ),
        serialization_alias="LA1.4",
        title="facility (HD)",
    )

    la1_5: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "la1_5",
            "location_status",
            "LA1.5",
        ),
        serialization_alias="LA1.5",
        title="location status",
    )

    la1_6: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "la1_6",
            "person_location_type",
            "LA1.6",
        ),
        serialization_alias="LA1.6",
        title="person location type",
    )

    la1_7: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "la1_7",
            "building",
            "LA1.7",
        ),
        serialization_alias="LA1.7",
        title="building",
    )

    la1_8: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "la1_8",
            "floor",
            "LA1.8",
        ),
        serialization_alias="LA1.8",
        title="floor",
    )

    la1_9: AD | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "la1_9",
            "address",
            "LA1.9",
        ),
        serialization_alias="LA1.9",
        title="address",
    )

    model_config = {"populate_by_name": True}
