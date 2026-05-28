"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: PL
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from .HD import HD


class PL(BaseModel):
    """HL7 v2 PL data type."""

    pl_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pl_1",
            "point_of_care",
            "PL.1",
        ),
        serialization_alias="PL.1",
        title="point of care",
    )

    pl_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pl_2",
            "room",
            "PL.2",
        ),
        serialization_alias="PL.2",
        title="room",
    )

    pl_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pl_3",
            "bed",
            "PL.3",
        ),
        serialization_alias="PL.3",
        title="bed",
    )

    pl_4: Optional[HD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pl_4",
            "facility_hd",
            "PL.4",
        ),
        serialization_alias="PL.4",
        title="facility (HD)",
    )

    pl_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pl_5",
            "location_status",
            "PL.5",
        ),
        serialization_alias="PL.5",
        title="location status",
    )

    pl_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pl_6",
            "person_location_type",
            "PL.6",
        ),
        serialization_alias="PL.6",
        title="person location type",
    )

    pl_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pl_7",
            "building",
            "PL.7",
        ),
        serialization_alias="PL.7",
        title="building",
    )

    pl_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pl_8",
            "floor",
            "PL.8",
        ),
        serialization_alias="PL.8",
        title="floor",
    )

    pl_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pl_9",
            "location_description",
            "PL.9",
        ),
        serialization_alias="PL.9",
        title="Location description",
    )

    model_config = {"populate_by_name": True}
