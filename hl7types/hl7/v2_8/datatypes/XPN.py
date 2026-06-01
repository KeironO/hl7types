"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: XPN
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model
from pydantic import field_validator

from .CWE import CWE
from .FN import FN


class XPN(HL7Model):
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

    xpn_7 : str | None
        XPN.7 (opt) - Name Type Code (ID)

    xpn_8 : str | None
        XPN.8 (opt) - Name Representation Code (ID)

    xpn_9 : CWE | None
        XPN.9 (opt) - Name Context (CWE)

    xpn_11 : str | None
        XPN.11 (opt) - Name Assembly Order (ID)

    xpn_12 : str | None
        XPN.12 (opt) - Effective Date (DTM)

    xpn_13 : str | None
        XPN.13 (opt) - Expiration Date (DTM)

    xpn_14 : str | None
        XPN.14 (opt) - Professional Suffix (ST)

    xpn_15 : str | None
        XPN.15 (opt) - Called By (ST)
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

    xpn_7: Optional[str] = Field(
        default=None,
        max_length=5,
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
        max_length=1,
        validation_alias=AliasChoices(
            "xpn_8",
            "name_representation_code",
            "XPN.8",
        ),
        serialization_alias="XPN.8",
        title="Name Representation Code",
    )

    xpn_9: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xpn_9",
            "name_context",
            "XPN.9",
        ),
        serialization_alias="XPN.9",
        title="Name Context",
    )

    xpn_11: Optional[str] = Field(
        default=None,
        max_length=1,
        validation_alias=AliasChoices(
            "xpn_11",
            "name_assembly_order",
            "XPN.11",
        ),
        serialization_alias="XPN.11",
        title="Name Assembly Order",
    )

    xpn_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xpn_12",
            "effective_date",
            "XPN.12",
        ),
        serialization_alias="XPN.12",
        title="Effective Date",
    )

    xpn_13: Optional[str] = Field(
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

    xpn_15: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xpn_15",
            "called_by",
            "XPN.15",
        ),
        serialization_alias="XPN.15",
        title="Called By",
    )

    @field_validator("xpn_12", "xpn_13", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?', v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 datetime")
        return v

    model_config = {"populate_by_name": True}
