"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: XAD
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from .DR import DR
from .SAD import SAD
from .TS import TS


class XAD(BaseModel):
    """HL7 v2 XAD data type."""

    xad_1: Optional[SAD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xad_1",
            "street_address",
            "XAD.1",
        ),
        serialization_alias="XAD.1",
        title="Street Address",
    )

    xad_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xad_2",
            "other_designation",
            "XAD.2",
        ),
        serialization_alias="XAD.2",
        title="Other Designation",
    )

    xad_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xad_3",
            "city",
            "XAD.3",
        ),
        serialization_alias="XAD.3",
        title="City",
    )

    xad_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xad_4",
            "state_or_province",
            "XAD.4",
        ),
        serialization_alias="XAD.4",
        title="State or Province",
    )

    xad_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xad_5",
            "zip_or_postal_code",
            "XAD.5",
        ),
        serialization_alias="XAD.5",
        title="Zip or Postal Code",
    )

    xad_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xad_6",
            "country",
            "XAD.6",
        ),
        serialization_alias="XAD.6",
        title="Country",
    )

    xad_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xad_7",
            "address_type",
            "XAD.7",
        ),
        serialization_alias="XAD.7",
        title="Address Type",
    )

    xad_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xad_8",
            "other_geographic_designation",
            "XAD.8",
        ),
        serialization_alias="XAD.8",
        title="Other Geographic Designation",
    )

    xad_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xad_9",
            "county_parish_code",
            "XAD.9",
        ),
        serialization_alias="XAD.9",
        title="County/Parish Code",
    )

    xad_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xad_10",
            "census_tract",
            "XAD.10",
        ),
        serialization_alias="XAD.10",
        title="Census Tract",
    )

    xad_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xad_11",
            "address_representation_code",
            "XAD.11",
        ),
        serialization_alias="XAD.11",
        title="Address Representation Code",
    )

    xad_12: Optional[DR] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xad_12",
            "address_validity_range",
            "XAD.12",
        ),
        serialization_alias="XAD.12",
        title="Address Validity Range",
    )

    xad_13: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xad_13",
            "effective_date",
            "XAD.13",
        ),
        serialization_alias="XAD.13",
        title="Effective Date",
    )

    xad_14: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xad_14",
            "expiration_date",
            "XAD.14",
        ),
        serialization_alias="XAD.14",
        title="Expiration Date",
    )

    model_config = {"populate_by_name": True}
