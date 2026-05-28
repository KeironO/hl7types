"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: PL
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from .EI import EI
from .HD import HD


class PL(BaseModel):
    """HL7 v2 PL data type."""

    pl_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pl_1",
            "point_of_care",
            "PL.1",
        ),
        serialization_alias="PL.1",
        title="Point of Care",
    )

    pl_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pl_2",
            "room",
            "PL.2",
        ),
        serialization_alias="PL.2",
        title="Room",
    )

    pl_3: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pl_3",
            "bed",
            "PL.3",
        ),
        serialization_alias="PL.3",
        title="Bed",
    )

    pl_4: HD | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pl_4",
            "facility",
            "PL.4",
        ),
        serialization_alias="PL.4",
        title="Facility",
    )

    pl_5: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pl_5",
            "location_status",
            "PL.5",
        ),
        serialization_alias="PL.5",
        title="Location Status",
    )

    pl_6: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pl_6",
            "person_location_type",
            "PL.6",
        ),
        serialization_alias="PL.6",
        title="Person Location Type",
    )

    pl_7: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pl_7",
            "building",
            "PL.7",
        ),
        serialization_alias="PL.7",
        title="Building",
    )

    pl_8: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pl_8",
            "floor",
            "PL.8",
        ),
        serialization_alias="PL.8",
        title="Floor",
    )

    pl_9: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pl_9",
            "location_description",
            "PL.9",
        ),
        serialization_alias="PL.9",
        title="Location Description",
    )

    pl_10: EI | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pl_10",
            "comprehensive_location_identifier",
            "PL.10",
        ),
        serialization_alias="PL.10",
        title="Comprehensive Location Identifier",
    )

    pl_11: HD | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pl_11",
            "assigning_authority_for_location",
            "PL.11",
        ),
        serialization_alias="PL.11",
        title="Assigning Authority for Location",
    )

    model_config = {"populate_by_name": True}
