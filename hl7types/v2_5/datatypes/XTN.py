"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: XTN
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field


class XTN(BaseModel):
    """HL7 v2 XTN data type."""

    xtn_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xtn_1",
            "telephone_number",
            "XTN.1",
        ),
        serialization_alias="XTN.1",
        title="Telephone Number",
    )

    xtn_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xtn_2",
            "telecommunication_use_code",
            "XTN.2",
        ),
        serialization_alias="XTN.2",
        title="Telecommunication Use Code",
    )

    xtn_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xtn_3",
            "telecommunication_equipment_type",
            "XTN.3",
        ),
        serialization_alias="XTN.3",
        title="Telecommunication Equipment Type",
    )

    xtn_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xtn_4",
            "email_address",
            "XTN.4",
        ),
        serialization_alias="XTN.4",
        title="Email Address",
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
        title="Area/City Code",
    )

    xtn_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xtn_7",
            "local_number",
            "XTN.7",
        ),
        serialization_alias="XTN.7",
        title="Local Number",
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
        title="Any Text",
    )

    xtn_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xtn_10",
            "extension_prefix",
            "XTN.10",
        ),
        serialization_alias="XTN.10",
        title="Extension Prefix",
    )

    xtn_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xtn_11",
            "speed_dial_code",
            "XTN.11",
        ),
        serialization_alias="XTN.11",
        title="Speed Dial Code",
    )

    xtn_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xtn_12",
            "unformatted_telephone_number",
            "XTN.12",
        ),
        serialization_alias="XTN.12",
        title="Unformatted Telephone number",
    )

    model_config = {"populate_by_name": True}
