"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: PN
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from .FN import FN


class PN(BaseModel):
    """HL7 v2 PN data type."""

    pn_1: FN | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pn_1",
            "family_last_name",
            "PN.1",
        ),
        serialization_alias="PN.1",
        title="family+last name",
    )

    pn_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pn_2",
            "given_name",
            "PN.2",
        ),
        serialization_alias="PN.2",
        title="given name",
    )

    pn_3: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pn_3",
            "middle_initial_or_name",
            "PN.3",
        ),
        serialization_alias="PN.3",
        title="middle initial or name",
    )

    pn_4: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pn_4",
            "suffix_e_g_jr_or_iii",
            "PN.4",
        ),
        serialization_alias="PN.4",
        title="suffix (e.g., JR or III)",
    )

    pn_5: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pn_5",
            "prefix_e_g_dr",
            "PN.5",
        ),
        serialization_alias="PN.5",
        title="prefix (e.g., DR)",
    )

    pn_6: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "pn_6",
            "degree_e_g_md",
            "PN.6",
        ),
        serialization_alias="PN.6",
        title="degree (e.g., MD)",
    )

    model_config = {"populate_by_name": True}
