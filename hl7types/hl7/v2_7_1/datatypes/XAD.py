"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: XAD
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from .CWE import CWE
from .EI import EI
from .SAD import SAD


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

    xad_9: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xad_9",
            "county_parish_code",
            "XAD.9",
        ),
        serialization_alias="XAD.9",
        title="County/Parish Code",
    )

    xad_10: Optional[CWE] = Field(
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

    xad_13: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xad_13",
            "effective_date",
            "XAD.13",
        ),
        serialization_alias="XAD.13",
        title="Effective Date",
    )

    xad_14: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xad_14",
            "expiration_date",
            "XAD.14",
        ),
        serialization_alias="XAD.14",
        title="Expiration Date",
    )

    xad_15: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xad_15",
            "expiration_reason",
            "XAD.15",
        ),
        serialization_alias="XAD.15",
        title="Expiration Reason",
    )

    xad_16: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xad_16",
            "temporary_indicator",
            "XAD.16",
        ),
        serialization_alias="XAD.16",
        title="Temporary Indicator",
    )

    xad_17: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xad_17",
            "bad_address_indicator",
            "XAD.17",
        ),
        serialization_alias="XAD.17",
        title="Bad Address Indicator",
    )

    xad_18: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xad_18",
            "address_usage",
            "XAD.18",
        ),
        serialization_alias="XAD.18",
        title="Address Usage",
    )

    xad_19: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xad_19",
            "addressee",
            "XAD.19",
        ),
        serialization_alias="XAD.19",
        title="Addressee",
    )

    xad_20: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xad_20",
            "comment",
            "XAD.20",
        ),
        serialization_alias="XAD.20",
        title="Comment",
    )

    xad_21: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xad_21",
            "preference_order",
            "XAD.21",
        ),
        serialization_alias="XAD.21",
        title="Preference Order",
    )

    xad_22: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xad_22",
            "protection_code",
            "XAD.22",
        ),
        serialization_alias="XAD.22",
        title="Protection Code",
    )

    xad_23: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xad_23",
            "address_identifier",
            "XAD.23",
        ),
        serialization_alias="XAD.23",
        title="Address Identifier",
    )

    model_config = {"populate_by_name": True}
