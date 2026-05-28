"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
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
            "point_of_care",
            "LA1.1",
        ),
        serialization_alias="LA1.1",
        title="Point of Care",
    )

    la1_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "la1_2",
            "room",
            "LA1.2",
        ),
        serialization_alias="LA1.2",
        title="Room",
    )

    la1_3: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "la1_3",
            "bed",
            "LA1.3",
        ),
        serialization_alias="LA1.3",
        title="Bed",
    )

    la1_4: HD | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "la1_4",
            "facility",
            "LA1.4",
        ),
        serialization_alias="LA1.4",
        title="Facility",
    )

    la1_5: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "la1_5",
            "location_status",
            "LA1.5",
        ),
        serialization_alias="LA1.5",
        title="Location Status",
    )

    la1_6: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "la1_6",
            "patient_location_type",
            "LA1.6",
        ),
        serialization_alias="LA1.6",
        title="Patient Location Type",
    )

    la1_7: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "la1_7",
            "building",
            "LA1.7",
        ),
        serialization_alias="LA1.7",
        title="Building",
    )

    la1_8: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "la1_8",
            "floor",
            "LA1.8",
        ),
        serialization_alias="LA1.8",
        title="Floor",
    )

    la1_9: AD | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "la1_9",
            "address",
            "LA1.9",
        ),
        serialization_alias="LA1.9",
        title="Address",
    )

    model_config = {"populate_by_name": True}
