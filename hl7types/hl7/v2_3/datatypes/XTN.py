"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: XTN
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field


class XTN(BaseModel):
    """HL7 v2 XTN data type.

    Attributes
    ----------
    xtn_1 : str | None
        XTN.1 (opt) - [(999)] 999-9999 [X99999][C any text] (TN)

    xtn_2 : str | None
        XTN.2 (opt) - telecommunication use code (ID)

    xtn_3 : str | None
        XTN.3 (opt) - telecommunication equipment type (ID) (ID)

    xtn_4 : str | None
        XTN.4 (opt) - Email address (ST)

    xtn_5 : str | None
        XTN.5 (opt) - Country Code (NM)

    xtn_6 : str | None
        XTN.6 (opt) - Area/city code (NM)

    xtn_7 : str | None
        XTN.7 (opt) - Phone number (NM)

    xtn_8 : str | None
        XTN.8 (opt) - Extension (NM)

    xtn_9 : str | None
        XTN.9 (opt) - any text (ST)
    """

    xtn_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xtn_1",
            "field_999_999_9999_x99999_c_any_text",
            "XTN.1",
        ),
        serialization_alias="XTN.1",
        title="[(999)] 999-9999 [X99999][C any text]",
    )

    xtn_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xtn_2",
            "telecommunication_use_code",
            "XTN.2",
        ),
        serialization_alias="XTN.2",
        title="telecommunication use code",
    )

    xtn_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xtn_3",
            "telecommunication_equipment_type_id",
            "XTN.3",
        ),
        serialization_alias="XTN.3",
        title="telecommunication equipment type (ID)",
    )

    xtn_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xtn_4",
            "email_address",
            "XTN.4",
        ),
        serialization_alias="XTN.4",
        title="Email address",
    )

    xtn_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xtn_5",
            "country_code",
            "XTN.5",
        ),
        serialization_alias="XTN.5",
        title="Country Code",
    )

    xtn_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xtn_6",
            "area_city_code",
            "XTN.6",
        ),
        serialization_alias="XTN.6",
        title="Area/city code",
    )

    xtn_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xtn_7",
            "phone_number",
            "XTN.7",
        ),
        serialization_alias="XTN.7",
        title="Phone number",
    )

    xtn_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xtn_8",
            "extension",
            "XTN.8",
        ),
        serialization_alias="XTN.8",
        title="Extension",
    )

    xtn_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xtn_9",
            "any_text",
            "XTN.9",
        ),
        serialization_alias="XTN.9",
        title="any text",
    )

    model_config = {"populate_by_name": True}
