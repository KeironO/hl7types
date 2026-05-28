"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: PPN
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from .CWE import CWE
from .FN import FN
from .HD import HD


class PPN(BaseModel):
    """HL7 v2 PPN data type."""

    ppn_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ppn_1",
            "person_identifier",
            "PPN.1",
        ),
        serialization_alias="PPN.1",
        title="Person Identifier",
    )

    ppn_2: Optional[FN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ppn_2",
            "family_name",
            "PPN.2",
        ),
        serialization_alias="PPN.2",
        title="Family Name",
    )

    ppn_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ppn_3",
            "given_name",
            "PPN.3",
        ),
        serialization_alias="PPN.3",
        title="Given Name",
    )

    ppn_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ppn_4",
            "second_and_further_given_names_or_initials_thereof",
            "PPN.4",
        ),
        serialization_alias="PPN.4",
        title="Second and Further Given Names or Initials Thereof",
    )

    ppn_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ppn_5",
            "suffix_e_g_jr_or_iii",
            "PPN.5",
        ),
        serialization_alias="PPN.5",
        title="Suffix (e.g., JR or III)",
    )

    ppn_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ppn_6",
            "prefix_e_g_dr",
            "PPN.6",
        ),
        serialization_alias="PPN.6",
        title="Prefix (e.g., DR)",
    )

    ppn_8: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ppn_8",
            "source_table",
            "PPN.8",
        ),
        serialization_alias="PPN.8",
        title="Source Table",
    )

    ppn_9: Optional[HD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ppn_9",
            "assigning_authority",
            "PPN.9",
        ),
        serialization_alias="PPN.9",
        title="Assigning Authority",
    )

    ppn_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ppn_10",
            "name_type_code",
            "PPN.10",
        ),
        serialization_alias="PPN.10",
        title="Name Type Code",
    )

    ppn_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ppn_11",
            "identifier_check_digit",
            "PPN.11",
        ),
        serialization_alias="PPN.11",
        title="Identifier Check Digit",
    )

    ppn_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ppn_12",
            "check_digit_scheme",
            "PPN.12",
        ),
        serialization_alias="PPN.12",
        title="Check Digit Scheme",
    )

    ppn_13: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ppn_13",
            "identifier_type_code",
            "PPN.13",
        ),
        serialization_alias="PPN.13",
        title="Identifier Type Code",
    )

    ppn_14: Optional[HD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ppn_14",
            "assigning_facility",
            "PPN.14",
        ),
        serialization_alias="PPN.14",
        title="Assigning Facility",
    )

    ppn_15: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ppn_15",
            "date_time_action_performed",
            "PPN.15",
        ),
        serialization_alias="PPN.15",
        title="Date/Time Action Performed",
    )

    ppn_16: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ppn_16",
            "name_representation_code",
            "PPN.16",
        ),
        serialization_alias="PPN.16",
        title="Name Representation Code",
    )

    ppn_17: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ppn_17",
            "name_context",
            "PPN.17",
        ),
        serialization_alias="PPN.17",
        title="Name Context",
    )

    ppn_19: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ppn_19",
            "name_assembly_order",
            "PPN.19",
        ),
        serialization_alias="PPN.19",
        title="Name Assembly Order",
    )

    ppn_20: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ppn_20",
            "effective_date",
            "PPN.20",
        ),
        serialization_alias="PPN.20",
        title="Effective Date",
    )

    ppn_21: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ppn_21",
            "expiration_date",
            "PPN.21",
        ),
        serialization_alias="PPN.21",
        title="Expiration Date",
    )

    ppn_22: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ppn_22",
            "professional_suffix",
            "PPN.22",
        ),
        serialization_alias="PPN.22",
        title="Professional Suffix",
    )

    ppn_23: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ppn_23",
            "assigning_jurisdiction",
            "PPN.23",
        ),
        serialization_alias="PPN.23",
        title="Assigning Jurisdiction",
    )

    ppn_24: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ppn_24",
            "assigning_agency_or_department",
            "PPN.24",
        ),
        serialization_alias="PPN.24",
        title="Assigning Agency or Department",
    )

    ppn_25: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ppn_25",
            "security_check",
            "PPN.25",
        ),
        serialization_alias="PPN.25",
        title="Security Check",
    )

    ppn_26: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ppn_26",
            "security_check_scheme",
            "PPN.26",
        ),
        serialization_alias="PPN.26",
        title="Security Check Scheme",
    )

    model_config = {"populate_by_name": True}
