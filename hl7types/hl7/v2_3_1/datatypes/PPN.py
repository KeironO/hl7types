"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: PPN
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from .FN import FN
from .HD import HD
from .TS import TS


class PPN(BaseModel):
    """HL7 v2 PPN data type."""

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
            "family_last_name",
            "PPN.2",
        ),
        serialization_alias="PPN.2",
        title="family+last name",
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
            "middle_initial_or_name",
            "PPN.4",
        ),
        serialization_alias="PPN.4",
        title="middle initial or name",
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
            "identifier_type_code",
            "PPN.13",
        ),
        serialization_alias="PPN.13",
        title="identifier type code",
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

    model_config = {"populate_by_name": True}
