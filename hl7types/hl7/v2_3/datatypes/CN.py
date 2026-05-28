"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: CN
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from .HD import HD


class CN(BaseModel):
    """HL7 v2 CN data type."""

    cn_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cn_1",
            "id_number_st",
            "CN.1",
        ),
        serialization_alias="CN.1",
        title="ID number (ST)",
    )

    cn_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cn_2",
            "family_name",
            "CN.2",
        ),
        serialization_alias="CN.2",
        title="family name",
    )

    cn_3: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cn_3",
            "given_name",
            "CN.3",
        ),
        serialization_alias="CN.3",
        title="given name",
    )

    cn_4: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cn_4",
            "middle_initial_or_name",
            "CN.4",
        ),
        serialization_alias="CN.4",
        title="middle initial or name",
    )

    cn_5: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cn_5",
            "suffix_e_g_jr_or_iii",
            "CN.5",
        ),
        serialization_alias="CN.5",
        title="suffix (e.g., JR or III)",
    )

    cn_6: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cn_6",
            "prefix_e_g_dr",
            "CN.6",
        ),
        serialization_alias="CN.6",
        title="prefix (e.g., DR)",
    )

    cn_7: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cn_7",
            "degree_e_g_md",
            "CN.7",
        ),
        serialization_alias="CN.7",
        title="degree (e.g., MD)",
    )

    cn_8: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cn_8",
            "source_table",
            "CN.8",
        ),
        serialization_alias="CN.8",
        title="source table",
    )

    cn_9: HD | None = Field(
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
