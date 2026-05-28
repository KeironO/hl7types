"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: XPN
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from .CWE import CWE
from .FN import FN


class XPN(BaseModel):
    """HL7 v2 XPN data type."""

    xpn_1: FN | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "xpn_1",
            "family_name",
            "XPN.1",
        ),
        serialization_alias="XPN.1",
        title="Family Name",
    )

    xpn_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "xpn_2",
            "given_name",
            "XPN.2",
        ),
        serialization_alias="XPN.2",
        title="Given Name",
    )

    xpn_3: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "xpn_3",
            "second_and_further_given_names_or_initials_thereof",
            "XPN.3",
        ),
        serialization_alias="XPN.3",
        title="Second and Further Given Names or Initials Thereof",
    )

    xpn_4: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "xpn_4",
            "suffix_e_g_jr_or_iii",
            "XPN.4",
        ),
        serialization_alias="XPN.4",
        title="Suffix (e.g., JR or III)",
    )

    xpn_5: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "xpn_5",
            "prefix_e_g_dr",
            "XPN.5",
        ),
        serialization_alias="XPN.5",
        title="Prefix (e.g., DR)",
    )

    xpn_7: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "xpn_7",
            "name_type_code",
            "XPN.7",
        ),
        serialization_alias="XPN.7",
        title="Name Type Code",
    )

    xpn_8: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "xpn_8",
            "name_representation_code",
            "XPN.8",
        ),
        serialization_alias="XPN.8",
        title="Name Representation Code",
    )

    xpn_9: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "xpn_9",
            "name_context",
            "XPN.9",
        ),
        serialization_alias="XPN.9",
        title="Name Context",
    )

    xpn_11: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "xpn_11",
            "name_assembly_order",
            "XPN.11",
        ),
        serialization_alias="XPN.11",
        title="Name Assembly Order",
    )

    xpn_12: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "xpn_12",
            "effective_date",
            "XPN.12",
        ),
        serialization_alias="XPN.12",
        title="Effective Date",
    )

    xpn_13: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "xpn_13",
            "expiration_date",
            "XPN.13",
        ),
        serialization_alias="XPN.13",
        title="Expiration Date",
    )

    xpn_14: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "xpn_14",
            "professional_suffix",
            "XPN.14",
        ),
        serialization_alias="XPN.14",
        title="Professional Suffix",
    )

    xpn_15: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "xpn_15",
            "called_by",
            "XPN.15",
        ),
        serialization_alias="XPN.15",
        title="Called By",
    )

    model_config = {"populate_by_name": True}
