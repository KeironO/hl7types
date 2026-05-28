"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: XPN
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from .FN import FN


class XPN(BaseModel):
    """HL7 v2 XPN data type."""

    xpn_1: Optional[FN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xpn_1",
            "family_last_name",
            "XPN.1",
        ),
        serialization_alias="XPN.1",
        title="family+last name",
    )

    xpn_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xpn_2",
            "given_name",
            "XPN.2",
        ),
        serialization_alias="XPN.2",
        title="given name",
    )

    xpn_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xpn_3",
            "middle_initial_or_name",
            "XPN.3",
        ),
        serialization_alias="XPN.3",
        title="middle initial or name",
    )

    xpn_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xpn_4",
            "suffix_e_g_jr_or_iii",
            "XPN.4",
        ),
        serialization_alias="XPN.4",
        title="suffix (e.g., JR or III)",
    )

    xpn_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xpn_5",
            "prefix_e_g_dr",
            "XPN.5",
        ),
        serialization_alias="XPN.5",
        title="prefix (e.g., DR)",
    )

    xpn_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xpn_6",
            "degree_e_g_md",
            "XPN.6",
        ),
        serialization_alias="XPN.6",
        title="degree (e.g., MD)",
    )

    xpn_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xpn_7",
            "name_type_code",
            "XPN.7",
        ),
        serialization_alias="XPN.7",
        title="name type code",
    )

    xpn_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xpn_8",
            "name_representation_code",
            "XPN.8",
        ),
        serialization_alias="XPN.8",
        title="Name Representation code",
    )

    model_config = {"populate_by_name": True}
