"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: LA2
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from .HD import HD


class LA2(BaseModel):
    """HL7 v2 LA2 data type."""

    la2_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "la2_1",
            "point_of_care",
            "LA2.1",
        ),
        serialization_alias="LA2.1",
        title="Point of Care",
    )

    la2_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "la2_2",
            "room",
            "LA2.2",
        ),
        serialization_alias="LA2.2",
        title="Room",
    )

    la2_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "la2_3",
            "bed",
            "LA2.3",
        ),
        serialization_alias="LA2.3",
        title="Bed",
    )

    la2_4: Optional[HD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "la2_4",
            "facility",
            "LA2.4",
        ),
        serialization_alias="LA2.4",
        title="Facility",
    )

    la2_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "la2_5",
            "location_status",
            "LA2.5",
        ),
        serialization_alias="LA2.5",
        title="Location Status",
    )

    la2_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "la2_6",
            "patient_location_type",
            "LA2.6",
        ),
        serialization_alias="LA2.6",
        title="Patient Location Type",
    )

    la2_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "la2_7",
            "building",
            "LA2.7",
        ),
        serialization_alias="LA2.7",
        title="Building",
    )

    la2_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "la2_8",
            "floor",
            "LA2.8",
        ),
        serialization_alias="LA2.8",
        title="Floor",
    )

    la2_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "la2_9",
            "street_address",
            "LA2.9",
        ),
        serialization_alias="LA2.9",
        title="Street Address",
    )

    la2_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "la2_10",
            "other_designation",
            "LA2.10",
        ),
        serialization_alias="LA2.10",
        title="Other Designation",
    )

    la2_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "la2_11",
            "city",
            "LA2.11",
        ),
        serialization_alias="LA2.11",
        title="City",
    )

    la2_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "la2_12",
            "state_or_province",
            "LA2.12",
        ),
        serialization_alias="LA2.12",
        title="State or Province",
    )

    la2_13: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "la2_13",
            "zip_or_postal_code",
            "LA2.13",
        ),
        serialization_alias="LA2.13",
        title="Zip or Postal Code",
    )

    la2_14: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "la2_14",
            "country",
            "LA2.14",
        ),
        serialization_alias="LA2.14",
        title="Country",
    )

    la2_15: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "la2_15",
            "address_type",
            "LA2.15",
        ),
        serialization_alias="LA2.15",
        title="Address Type",
    )

    la2_16: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "la2_16",
            "other_geographic_designation",
            "LA2.16",
        ),
        serialization_alias="LA2.16",
        title="Other Geographic Designation",
    )

    model_config = {"populate_by_name": True}
