"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: AD
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field


class AD(BaseModel):
    """HL7 v2 AD data type."""

    ad_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ad_1",
            "street_address",
            "AD.1",
        ),
        serialization_alias="AD.1",
        title="Street Address",
    )

    ad_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ad_2",
            "other_designation",
            "AD.2",
        ),
        serialization_alias="AD.2",
        title="Other Designation",
    )

    ad_3: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ad_3",
            "city",
            "AD.3",
        ),
        serialization_alias="AD.3",
        title="City",
    )

    ad_4: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ad_4",
            "state_or_province",
            "AD.4",
        ),
        serialization_alias="AD.4",
        title="State or Province",
    )

    ad_5: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ad_5",
            "zip_or_postal_code",
            "AD.5",
        ),
        serialization_alias="AD.5",
        title="Zip or Postal Code",
    )

    ad_6: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ad_6",
            "country",
            "AD.6",
        ),
        serialization_alias="AD.6",
        title="Country",
    )

    ad_7: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ad_7",
            "address_type",
            "AD.7",
        ),
        serialization_alias="AD.7",
        title="Address Type",
    )

    ad_8: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ad_8",
            "other_geographic_designation",
            "AD.8",
        ),
        serialization_alias="AD.8",
        title="Other Geographic Designation",
    )

    model_config = {"populate_by_name": True}
