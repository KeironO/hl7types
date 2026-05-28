"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: CN
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from .FN import FN
from .HD import HD


class CN(BaseModel):
    """HL7 v2 CN data type."""

    cn_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cn_1",
            "id_number_st",
            "CN.1",
        ),
        serialization_alias="CN.1",
        title="ID number (ST)",
    )

    cn_2: Optional[FN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cn_2",
            "family_name",
            "CN.2",
        ),
        serialization_alias="CN.2",
        title="family name",
    )

    cn_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cn_3",
            "given_name",
            "CN.3",
        ),
        serialization_alias="CN.3",
        title="given name",
    )

    cn_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cn_4",
            "second_and_further_given_names_or_initials_thereof",
            "CN.4",
        ),
        serialization_alias="CN.4",
        title="second and further given names or initials thereof",
    )

    cn_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cn_5",
            "suffix_e_g_jr_or_iii",
            "CN.5",
        ),
        serialization_alias="CN.5",
        title="suffix (e.g., JR or III)",
    )

    cn_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cn_6",
            "prefix_e_g_dr",
            "CN.6",
        ),
        serialization_alias="CN.6",
        title="prefix (e.g., DR)",
    )

    cn_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cn_7",
            "degree_e_g_md",
            "CN.7",
        ),
        serialization_alias="CN.7",
        title="degree (e.g., MD)",
    )

    cn_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cn_8",
            "source_table",
            "CN.8",
        ),
        serialization_alias="CN.8",
        title="source table",
    )

    cn_9: Optional[HD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cn_9",
            "assigning_authority",
            "CN.9",
        ),
        serialization_alias="CN.9",
        title="assigning authority",
    )

    model_config = {"populate_by_name": True}
