"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: CM_LA1
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from .HD import HD


class CM_LA1(BaseModel):
    """HL7 v2 CM_LA1 data type."""

    cm_la1_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_la1_1",
            "point_of_care_st",
            "CM_LA1.1",
        ),
        serialization_alias="CM_LA1.1",
        title="point of care (ST)",
    )

    cm_la1_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_la1_2",
            "room",
            "CM_LA1.2",
        ),
        serialization_alias="CM_LA1.2",
        title="room",
    )

    cm_la1_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_la1_3",
            "bed",
            "CM_LA1.3",
        ),
        serialization_alias="CM_LA1.3",
        title="bed",
    )

    cm_la1_4: Optional[HD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_la1_4",
            "facility_hd",
            "CM_LA1.4",
        ),
        serialization_alias="CM_LA1.4",
        title="facility (HD)",
    )

    cm_la1_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_la1_5",
            "location_status",
            "CM_LA1.5",
        ),
        serialization_alias="CM_LA1.5",
        title="location status",
    )

    cm_la1_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_la1_6",
            "person_location_type",
            "CM_LA1.6",
        ),
        serialization_alias="CM_LA1.6",
        title="person location type",
    )

    cm_la1_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_la1_7",
            "building",
            "CM_LA1.7",
        ),
        serialization_alias="CM_LA1.7",
        title="building",
    )

    cm_la1_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_la1_8",
            "floor",
            "CM_LA1.8",
        ),
        serialization_alias="CM_LA1.8",
        title="floor",
    )

    cm_la1_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_la1_9",
            "street_address",
            "CM_LA1.9",
        ),
        serialization_alias="CM_LA1.9",
        title="street address",
    )

    cm_la1_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_la1_10",
            "other_designation",
            "CM_LA1.10",
        ),
        serialization_alias="CM_LA1.10",
        title="other designation",
    )

    cm_la1_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_la1_11",
            "city",
            "CM_LA1.11",
        ),
        serialization_alias="CM_LA1.11",
        title="city",
    )

    cm_la1_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_la1_12",
            "state_or_province",
            "CM_LA1.12",
        ),
        serialization_alias="CM_LA1.12",
        title="state or province",
    )

    cm_la1_13: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_la1_13",
            "zip_or_postal_code",
            "CM_LA1.13",
        ),
        serialization_alias="CM_LA1.13",
        title="zip or postal code",
    )

    cm_la1_14: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_la1_14",
            "country",
            "CM_LA1.14",
        ),
        serialization_alias="CM_LA1.14",
        title="country",
    )

    cm_la1_15: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_la1_15",
            "address_type",
            "CM_LA1.15",
        ),
        serialization_alias="CM_LA1.15",
        title="address type",
    )

    cm_la1_16: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_la1_16",
            "other_geographic_designation",
            "CM_LA1.16",
        ),
        serialization_alias="CM_LA1.16",
        title="other geographic designation",
    )

    model_config = {"populate_by_name": True}
