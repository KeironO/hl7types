"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: LA2
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from .HD import HD


class LA2(HL7Model):
    """HL7 v2 LA2 data type.

    Attributes
    ----------
    la2_1 : str | None
        LA2.1 (opt) - Point of Care (IS)

    la2_2 : str | None
        LA2.2 (opt) - Room (IS)

    la2_3 : str | None
        LA2.3 (opt) - Bed (IS)

    la2_4 : HD | None
        LA2.4 (opt) - Facility (HD)

    la2_5 : str | None
        LA2.5 (opt) - Location Status (IS)

    la2_6 : str | None
        LA2.6 (opt) - Patient Location Type (IS)

    la2_7 : str | None
        LA2.7 (opt) - Building (IS)

    la2_8 : str | None
        LA2.8 (opt) - Floor (IS)

    la2_9 : str | None
        LA2.9 (opt) - Street Address (ST)

    la2_10 : str | None
        LA2.10 (opt) - Other Designation (ST)

    la2_11 : str | None
        LA2.11 (opt) - City (ST)

    la2_12 : str | None
        LA2.12 (opt) - State or Province (ST)

    la2_13 : str | None
        LA2.13 (opt) - Zip or Postal Code (ST)

    la2_14 : str | None
        LA2.14 (opt) - Country (ID)

    la2_15 : str | None
        LA2.15 (opt) - Address Type (ID)

    la2_16 : str | None
        LA2.16 (opt) - Other Geographic Designation (ST)
    """

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
