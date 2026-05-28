"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: AD
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field


class AD(BaseModel):
    """HL7 v2 AD data type."""

    ad_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ad_1",
            "street_address",
            "AD.1",
        ),
        serialization_alias="AD.1",
        title="street address",
    )

    ad_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ad_2",
            "other_designation",
            "AD.2",
        ),
        serialization_alias="AD.2",
        title="other designation",
    )

    ad_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ad_3",
            "city",
            "AD.3",
        ),
        serialization_alias="AD.3",
        title="city",
    )

    ad_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ad_4",
            "state_or_province",
            "AD.4",
        ),
        serialization_alias="AD.4",
        title="state or province",
    )

    ad_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ad_5",
            "zip_or_postal_code",
            "AD.5",
        ),
        serialization_alias="AD.5",
        title="zip or postal code",
    )

    ad_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ad_6",
            "country",
            "AD.6",
        ),
        serialization_alias="AD.6",
        title="country",
    )

    ad_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ad_7",
            "address_type",
            "AD.7",
        ),
        serialization_alias="AD.7",
        title="address type",
    )

    ad_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ad_8",
            "other_geographic_designation",
            "AD.8",
        ),
        serialization_alias="AD.8",
        title="other geographic designation",
    )

    model_config = {"populate_by_name": True}
