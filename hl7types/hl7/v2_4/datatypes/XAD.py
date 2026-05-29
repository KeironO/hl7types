"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: XAD
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from .DR import DR
from .SAD import SAD


class XAD(BaseModel):
    """HL7 v2 XAD data type.

    Attributes
    ----------
    xad_1 : SAD | None
        XAD.1 (opt) - street address (SAD) (SAD)

    xad_2 : str | None
        XAD.2 (opt) - other designation (ST)

    xad_3 : str | None
        XAD.3 (opt) - city (ST)

    xad_4 : str | None
        XAD.4 (opt) - state or province (ST)

    xad_5 : str | None
        XAD.5 (opt) - zip or postal code (ST)

    xad_6 : str | None
        XAD.6 (opt) - country (ID)

    xad_7 : str | None
        XAD.7 (opt) - address type (ID)

    xad_8 : str | None
        XAD.8 (opt) - other geographic designation (ST)

    xad_9 : str | None
        XAD.9 (opt) - county/parish code (IS)

    xad_10 : str | None
        XAD.10 (opt) - census tract (IS)

    xad_11 : str | None
        XAD.11 (opt) - address representation code (ID)

    xad_12 : DR | None
        XAD.12 (opt) - address validity range (DR)
    """

    xad_1: Optional[SAD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xad_1",
            "street_address_sad",
            "XAD.1",
        ),
        serialization_alias="XAD.1",
        title="street address (SAD)",
    )

    xad_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xad_2",
            "other_designation",
            "XAD.2",
        ),
        serialization_alias="XAD.2",
        title="other designation",
    )

    xad_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xad_3",
            "city",
            "XAD.3",
        ),
        serialization_alias="XAD.3",
        title="city",
    )

    xad_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xad_4",
            "state_or_province",
            "XAD.4",
        ),
        serialization_alias="XAD.4",
        title="state or province",
    )

    xad_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xad_5",
            "zip_or_postal_code",
            "XAD.5",
        ),
        serialization_alias="XAD.5",
        title="zip or postal code",
    )

    xad_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xad_6",
            "country",
            "XAD.6",
        ),
        serialization_alias="XAD.6",
        title="country",
    )

    xad_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xad_7",
            "address_type",
            "XAD.7",
        ),
        serialization_alias="XAD.7",
        title="address type",
    )

    xad_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xad_8",
            "other_geographic_designation",
            "XAD.8",
        ),
        serialization_alias="XAD.8",
        title="other geographic designation",
    )

    xad_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xad_9",
            "county_parish_code",
            "XAD.9",
        ),
        serialization_alias="XAD.9",
        title="county/parish code",
    )

    xad_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xad_10",
            "census_tract",
            "XAD.10",
        ),
        serialization_alias="XAD.10",
        title="census tract",
    )

    xad_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xad_11",
            "address_representation_code",
            "XAD.11",
        ),
        serialization_alias="XAD.11",
        title="address representation code",
    )

    xad_12: Optional[DR] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xad_12",
            "address_validity_range",
            "XAD.12",
        ),
        serialization_alias="XAD.12",
        title="address validity range",
    )

    model_config = {"populate_by_name": True}
