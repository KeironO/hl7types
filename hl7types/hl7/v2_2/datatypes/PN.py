"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: PN
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field


class PN(BaseModel):
    """HL7 v2 PN data type.

    Attributes
    ----------
    pn_1 : str | None
        PN.1 (opt) - familiy name (ST)

    pn_2 : str | None
        PN.2 (opt) - given name (ST)

    pn_3 : str | None
        PN.3 (opt) - middle initial or name (ST)

    pn_4 : str | None
        PN.4 (opt) - suffix (e.g. JR or III) (ST)

    pn_5 : str | None
        PN.5 (opt) - prefix (e.g. DR) (ST)

    pn_6 : str | None
        PN.6 (opt) - degree (e.g. MD) (ST)
    """

    pn_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pn_1",
            "familiy_name",
            "PN.1",
        ),
        serialization_alias="PN.1",
        title="familiy name",
    )

    pn_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pn_2",
            "given_name",
            "PN.2",
        ),
        serialization_alias="PN.2",
        title="given name",
    )

    pn_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pn_3",
            "middle_initial_or_name",
            "PN.3",
        ),
        serialization_alias="PN.3",
        title="middle initial or name",
    )

    pn_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pn_4",
            "suffix_e_g_jr_or_iii",
            "PN.4",
        ),
        serialization_alias="PN.4",
        title="suffix (e.g. JR or III)",
    )

    pn_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pn_5",
            "prefix_e_g_dr",
            "PN.5",
        ),
        serialization_alias="PN.5",
        title="prefix (e.g. DR)",
    )

    pn_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pn_6",
            "degree_e_g_md",
            "PN.6",
        ),
        serialization_alias="PN.6",
        title="degree (e.g. MD)",
    )

    model_config = {"populate_by_name": True}
