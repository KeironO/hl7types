"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: PPN
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from .CE import CE
from .DR import DR
from .FN import FN
from .HD import HD
from .TS import TS


class PPN(HL7Model):
    """HL7 v2 PPN data type.

    Attributes
    ----------
    ppn_1 : str | None
        PPN.1 (opt) - ID number (ST) (ST)

    ppn_2 : FN | None
        PPN.2 (opt) - family name (FN)

    ppn_3 : str | None
        PPN.3 (opt) - given name (ST)

    ppn_4 : str | None
        PPN.4 (opt) - second and further given names or initials thereof (ST)

    ppn_5 : str | None
        PPN.5 (opt) - suffix (e.g., JR or III) (ST)

    ppn_6 : str | None
        PPN.6 (opt) - prefix (e.g., DR) (ST)

    ppn_7 : str | None
        PPN.7 (opt) - degree (e.g., MD) (IS)

    ppn_8 : str | None
        PPN.8 (opt) - source table (IS)

    ppn_9 : HD | None
        PPN.9 (opt) - assigning authority (HD)

    ppn_10 : str | None
        PPN.10 (opt) - name type code (ID)

    ppn_11 : str | None
        PPN.11 (opt) - identifier check digit (ST)

    ppn_12 : str | None
        PPN.12 (opt) - code identifying the check digit scheme employed (ID)

    ppn_13 : str | None
        PPN.13 (opt) - identifier type code (IS) (IS)

    ppn_14 : HD | None
        PPN.14 (opt) - assigning facility (HD)

    ppn_15 : TS | None
        PPN.15 (opt) - Date/Time Action Performed (TS)

    ppn_16 : str | None
        PPN.16 (opt) - Name Representation code (ID)

    ppn_17 : CE | None
        PPN.17 (opt) - name context (CE)

    ppn_18 : DR | None
        PPN.18 (opt) - name validity range (DR)

    ppn_19 : str | None
        PPN.19 (opt) - name assembly order (ID)
    """

    ppn_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ppn_1",
            "id_number_st",
            "PPN.1",
        ),
        serialization_alias="PPN.1",
        title="ID number (ST)",
    )

    ppn_2: Optional[FN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ppn_2",
            "family_name",
            "PPN.2",
        ),
        serialization_alias="PPN.2",
        title="family name",
    )

    ppn_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ppn_3",
            "given_name",
            "PPN.3",
        ),
        serialization_alias="PPN.3",
        title="given name",
    )

    ppn_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ppn_4",
            "second_and_further_given_names_or_initials_thereof",
            "PPN.4",
        ),
        serialization_alias="PPN.4",
        title="second and further given names or initials thereof",
    )

    ppn_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ppn_5",
            "suffix_e_g_jr_or_iii",
            "PPN.5",
        ),
        serialization_alias="PPN.5",
        title="suffix (e.g., JR or III)",
    )

    ppn_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ppn_6",
            "prefix_e_g_dr",
            "PPN.6",
        ),
        serialization_alias="PPN.6",
        title="prefix (e.g., DR)",
    )

    ppn_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ppn_7",
            "degree_e_g_md",
            "PPN.7",
        ),
        serialization_alias="PPN.7",
        title="degree (e.g., MD)",
    )

    ppn_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ppn_8",
            "source_table",
            "PPN.8",
        ),
        serialization_alias="PPN.8",
        title="source table",
    )

    ppn_9: Optional[HD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ppn_9",
            "assigning_authority",
            "PPN.9",
        ),
        serialization_alias="PPN.9",
        title="assigning authority",
    )

    ppn_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ppn_10",
            "name_type_code",
            "PPN.10",
        ),
        serialization_alias="PPN.10",
        title="name type code",
    )

    ppn_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ppn_11",
            "identifier_check_digit",
            "PPN.11",
        ),
        serialization_alias="PPN.11",
        title="identifier check digit",
    )

    ppn_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ppn_12",
            "code_identifying_the_check_digit_scheme_employed",
            "PPN.12",
        ),
        serialization_alias="PPN.12",
        title="code identifying the check digit scheme employed",
    )

    ppn_13: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ppn_13",
            "identifier_type_code_is",
            "PPN.13",
        ),
        serialization_alias="PPN.13",
        title="identifier type code (IS)",
    )

    ppn_14: Optional[HD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ppn_14",
            "assigning_facility",
            "PPN.14",
        ),
        serialization_alias="PPN.14",
        title="assigning facility",
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
        title="Name Representation code",
    )

    ppn_17: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ppn_17",
            "name_context",
            "PPN.17",
        ),
        serialization_alias="PPN.17",
        title="name context",
    )

    ppn_18: Optional[DR] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ppn_18",
            "name_validity_range",
            "PPN.18",
        ),
        serialization_alias="PPN.18",
        title="name validity range",
    )

    ppn_19: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ppn_19",
            "name_assembly_order",
            "PPN.19",
        ),
        serialization_alias="PPN.19",
        title="name assembly order",
    )

    model_config = {"populate_by_name": True}
