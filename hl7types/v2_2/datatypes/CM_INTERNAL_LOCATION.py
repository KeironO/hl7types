"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: CM_INTERNAL_LOCATION
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field


class CM_INTERNAL_LOCATION(BaseModel):
    """HL7 v2 CM_INTERNAL_LOCATION data type."""

    cm_internal_location_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_internal_location_1",
            "nurse_unit_station",
            "CM_INTERNAL_LOCATION.1",
        ),
        serialization_alias="CM_INTERNAL_LOCATION.1",
        title="nurse unit (Station)",
    )

    cm_internal_location_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_internal_location_2",
            "room",
            "CM_INTERNAL_LOCATION.2",
        ),
        serialization_alias="CM_INTERNAL_LOCATION.2",
        title="Room",
    )

    cm_internal_location_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_internal_location_3",
            "bed",
            "CM_INTERNAL_LOCATION.3",
        ),
        serialization_alias="CM_INTERNAL_LOCATION.3",
        title="Bed",
    )

    cm_internal_location_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_internal_location_4",
            "facility_id",
            "CM_INTERNAL_LOCATION.4",
        ),
        serialization_alias="CM_INTERNAL_LOCATION.4",
        title="Facility ID",
    )

    cm_internal_location_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_internal_location_5",
            "bed_status",
            "CM_INTERNAL_LOCATION.5",
        ),
        serialization_alias="CM_INTERNAL_LOCATION.5",
        title="Bed Status",
    )

    cm_internal_location_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_internal_location_6",
            "etage",
            "CM_INTERNAL_LOCATION.6",
        ),
        serialization_alias="CM_INTERNAL_LOCATION.6",
        title="Etage",
    )

    cm_internal_location_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_internal_location_7",
            "klinik",
            "CM_INTERNAL_LOCATION.7",
        ),
        serialization_alias="CM_INTERNAL_LOCATION.7",
        title="Klinik",
    )

    cm_internal_location_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_internal_location_8",
            "zentrum",
            "CM_INTERNAL_LOCATION.8",
        ),
        serialization_alias="CM_INTERNAL_LOCATION.8",
        title="Zentrum",
    )

    model_config = {"populate_by_name": True}
