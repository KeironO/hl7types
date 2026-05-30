"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: PPN
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from .CE import CE
from .CWE import CWE
from .DR import DR
from .FN import FN
from .HD import HD
from .TS import TS


class PPN(HL7Model):
    """HL7 v2 PPN data type.

    Attributes
    ----------
    ppn_1 : str | None
        PPN.1 (opt) - ID Number (ST)

    ppn_2 : FN | None
        PPN.2 (opt) - Family Name (FN)

    ppn_3 : str | None
        PPN.3 (opt) - Given Name (ST)

    ppn_4 : str | None
        PPN.4 (opt) - Second and Further Given Names or Initials Thereof (ST)

    ppn_5 : str | None
        PPN.5 (opt) - Suffix (e.g., JR or III) (ST)

    ppn_6 : str | None
        PPN.6 (opt) - Prefix (e.g., DR) (ST)

    ppn_7 : str | None
        PPN.7 (opt) - Degree (e.g., MD) (IS)

    ppn_8 : str | None
        PPN.8 (opt) - Source Table (IS)

    ppn_9 : HD | None
        PPN.9 (opt) - Assigning Authority (HD)

    ppn_10 : str | None
        PPN.10 (opt) - Name Type Code (ID)

    ppn_11 : str | None
        PPN.11 (opt) - Identifier Check Digit (ST)

    ppn_12 : str | None
        PPN.12 (opt) - Check Digit Scheme (ID)

    ppn_13 : str | None
        PPN.13 (opt) - Identifier Type Code (ID)

    ppn_14 : HD | None
        PPN.14 (opt) - Assigning Facility (HD)

    ppn_15 : TS | None
        PPN.15 (opt) - Date/Time Action Performed (TS)

    ppn_16 : str | None
        PPN.16 (opt) - Name Representation Code (ID)

    ppn_17 : CE | None
        PPN.17 (opt) - Name Context (CE)

    ppn_18 : DR | None
        PPN.18 (opt) - Name Validity Range (DR)

    ppn_19 : str | None
        PPN.19 (opt) - Name Assembly Order (ID)

    ppn_20 : TS | None
        PPN.20 (opt) - Effective Date (TS)

    ppn_21 : TS | None
        PPN.21 (opt) - Expiration Date (TS)

    ppn_22 : str | None
        PPN.22 (opt) - Professional Suffix (ST)

    ppn_23 : CWE | None
        PPN.23 (opt) - Assigning Jurisdiction (CWE)

    ppn_24 : CWE | None
        PPN.24 (opt) - Assigning Agency or Department (CWE)
    """

    ppn_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ppn_1",
            "id_number",
            "PPN.1",
        ),
        serialization_alias="PPN.1",
        title="ID Number",
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

    ppn_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ppn_7",
            "degree_e_g_md",
            "PPN.7",
        ),
        serialization_alias="PPN.7",
        title="Degree (e.g., MD)",
    )

    ppn_8: Optional[str] = Field(
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

    ppn_15: Optional[TS] = Field(
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

    ppn_17: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ppn_17",
            "name_context",
            "PPN.17",
        ),
        serialization_alias="PPN.17",
        title="Name Context",
    )

    ppn_18: Optional[DR] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ppn_18",
            "name_validity_range",
            "PPN.18",
        ),
        serialization_alias="PPN.18",
        title="Name Validity Range",
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

    ppn_20: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ppn_20",
            "effective_date",
            "PPN.20",
        ),
        serialization_alias="PPN.20",
        title="Effective Date",
    )

    ppn_21: Optional[TS] = Field(
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

    model_config = {"populate_by_name": True}
