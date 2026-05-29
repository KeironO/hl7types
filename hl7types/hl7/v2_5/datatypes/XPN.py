"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: XPN
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from .CE import CE
from .DR import DR
from .FN import FN
from .TS import TS


class XPN(BaseModel):
    """HL7 v2 XPN data type.

    Attributes
    ----------
    xpn_1 : FN | None
        XPN.1 (opt) - Family Name (FN)

    xpn_2 : str | None
        XPN.2 (opt) - Given Name (ST)

    xpn_3 : str | None
        XPN.3 (opt) - Second and Further Given Names or Initials Thereof (ST)

    xpn_4 : str | None
        XPN.4 (opt) - Suffix (e.g., JR or III) (ST)

    xpn_5 : str | None
        XPN.5 (opt) - Prefix (e.g., DR) (ST)

    xpn_6 : str | None
        XPN.6 (opt) - Degree (e.g., MD) (IS)

    xpn_7 : str | None
        XPN.7 (opt) - Name Type Code (ID)

    xpn_8 : str | None
        XPN.8 (opt) - Name Representation Code (ID)

    xpn_9 : CE | None
        XPN.9 (opt) - Name Context (CE)

    xpn_10 : DR | None
        XPN.10 (opt) - Name Validity Range (DR)

    xpn_11 : str | None
        XPN.11 (opt) - Name Assembly Order (ID)

    xpn_12 : TS | None
        XPN.12 (opt) - Effective Date (TS)

    xpn_13 : TS | None
        XPN.13 (opt) - Expiration Date (TS)

    xpn_14 : str | None
        XPN.14 (opt) - Professional Suffix (ST)
    """

    xpn_1: Optional[FN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xpn_1",
            "family_name",
            "XPN.1",
        ),
        serialization_alias="XPN.1",
        title="Family Name",
    )

    xpn_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xpn_2",
            "given_name",
            "XPN.2",
        ),
        serialization_alias="XPN.2",
        title="Given Name",
    )

    xpn_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xpn_3",
            "second_and_further_given_names_or_initials_thereof",
            "XPN.3",
        ),
        serialization_alias="XPN.3",
        title="Second and Further Given Names or Initials Thereof",
    )

    xpn_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xpn_4",
            "suffix_e_g_jr_or_iii",
            "XPN.4",
        ),
        serialization_alias="XPN.4",
        title="Suffix (e.g., JR or III)",
    )

    xpn_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xpn_5",
            "prefix_e_g_dr",
            "XPN.5",
        ),
        serialization_alias="XPN.5",
        title="Prefix (e.g., DR)",
    )

    xpn_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xpn_6",
            "degree_e_g_md",
            "XPN.6",
        ),
        serialization_alias="XPN.6",
        title="Degree (e.g., MD)",
    )

    xpn_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xpn_7",
            "name_type_code",
            "XPN.7",
        ),
        serialization_alias="XPN.7",
        title="Name Type Code",
    )

    xpn_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xpn_8",
            "name_representation_code",
            "XPN.8",
        ),
        serialization_alias="XPN.8",
        title="Name Representation Code",
    )

    xpn_9: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xpn_9",
            "name_context",
            "XPN.9",
        ),
        serialization_alias="XPN.9",
        title="Name Context",
    )

    xpn_10: Optional[DR] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xpn_10",
            "name_validity_range",
            "XPN.10",
        ),
        serialization_alias="XPN.10",
        title="Name Validity Range",
    )

    xpn_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xpn_11",
            "name_assembly_order",
            "XPN.11",
        ),
        serialization_alias="XPN.11",
        title="Name Assembly Order",
    )

    xpn_12: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xpn_12",
            "effective_date",
            "XPN.12",
        ),
        serialization_alias="XPN.12",
        title="Effective Date",
    )

    xpn_13: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xpn_13",
            "expiration_date",
            "XPN.13",
        ),
        serialization_alias="XPN.13",
        title="Expiration Date",
    )

    xpn_14: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xpn_14",
            "professional_suffix",
            "XPN.14",
        ),
        serialization_alias="XPN.14",
        title="Professional Suffix",
    )

    model_config = {"populate_by_name": True}
