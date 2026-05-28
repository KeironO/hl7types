"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: XCN
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from .CE import CE
from .CWE import CWE
from .DR import DR
from .FN import FN
from .HD import HD
from .TS import TS


class XCN(BaseModel):
    """HL7 v2 XCN data type."""

    xcn_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xcn_1",
            "id_number",
            "XCN.1",
        ),
        serialization_alias="XCN.1",
        title="ID Number",
    )

    xcn_2: Optional[FN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xcn_2",
            "family_name",
            "XCN.2",
        ),
        serialization_alias="XCN.2",
        title="Family Name",
    )

    xcn_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xcn_3",
            "given_name",
            "XCN.3",
        ),
        serialization_alias="XCN.3",
        title="Given Name",
    )

    xcn_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xcn_4",
            "second_and_further_given_names_or_initials_thereof",
            "XCN.4",
        ),
        serialization_alias="XCN.4",
        title="Second and Further Given Names or Initials Thereof",
    )

    xcn_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xcn_5",
            "suffix_e_g_jr_or_iii",
            "XCN.5",
        ),
        serialization_alias="XCN.5",
        title="Suffix (e.g., JR or III)",
    )

    xcn_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xcn_6",
            "prefix_e_g_dr",
            "XCN.6",
        ),
        serialization_alias="XCN.6",
        title="Prefix (e.g., DR)",
    )

    xcn_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xcn_7",
            "degree_e_g_md",
            "XCN.7",
        ),
        serialization_alias="XCN.7",
        title="Degree (e.g., MD)",
    )

    xcn_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xcn_8",
            "source_table",
            "XCN.8",
        ),
        serialization_alias="XCN.8",
        title="Source Table",
    )

    xcn_9: Optional[HD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xcn_9",
            "assigning_authority",
            "XCN.9",
        ),
        serialization_alias="XCN.9",
        title="Assigning Authority",
    )

    xcn_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xcn_10",
            "name_type_code",
            "XCN.10",
        ),
        serialization_alias="XCN.10",
        title="Name Type Code",
    )

    xcn_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xcn_11",
            "identifier_check_digit",
            "XCN.11",
        ),
        serialization_alias="XCN.11",
        title="Identifier Check Digit",
    )

    xcn_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xcn_12",
            "check_digit_scheme",
            "XCN.12",
        ),
        serialization_alias="XCN.12",
        title="Check Digit Scheme",
    )

    xcn_13: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xcn_13",
            "identifier_type_code",
            "XCN.13",
        ),
        serialization_alias="XCN.13",
        title="Identifier Type Code",
    )

    xcn_14: Optional[HD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xcn_14",
            "assigning_facility",
            "XCN.14",
        ),
        serialization_alias="XCN.14",
        title="Assigning Facility",
    )

    xcn_15: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xcn_15",
            "name_representation_code",
            "XCN.15",
        ),
        serialization_alias="XCN.15",
        title="Name Representation Code",
    )

    xcn_16: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xcn_16",
            "name_context",
            "XCN.16",
        ),
        serialization_alias="XCN.16",
        title="Name Context",
    )

    xcn_17: Optional[DR] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xcn_17",
            "name_validity_range",
            "XCN.17",
        ),
        serialization_alias="XCN.17",
        title="Name Validity Range",
    )

    xcn_18: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xcn_18",
            "name_assembly_order",
            "XCN.18",
        ),
        serialization_alias="XCN.18",
        title="Name Assembly Order",
    )

    xcn_19: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xcn_19",
            "effective_date",
            "XCN.19",
        ),
        serialization_alias="XCN.19",
        title="Effective Date",
    )

    xcn_20: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xcn_20",
            "expiration_date",
            "XCN.20",
        ),
        serialization_alias="XCN.20",
        title="Expiration Date",
    )

    xcn_21: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xcn_21",
            "professional_suffix",
            "XCN.21",
        ),
        serialization_alias="XCN.21",
        title="Professional Suffix",
    )

    xcn_22: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xcn_22",
            "assigning_jurisdiction",
            "XCN.22",
        ),
        serialization_alias="XCN.22",
        title="Assigning Jurisdiction",
    )

    xcn_23: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "xcn_23",
            "assigning_agency_or_department",
            "XCN.23",
        ),
        serialization_alias="XCN.23",
        title="Assigning Agency or Department",
    )

    model_config = {"populate_by_name": True}
