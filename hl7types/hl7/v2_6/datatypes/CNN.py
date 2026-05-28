"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: CNN
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field


class CNN(BaseModel):
    """HL7 v2 CNN data type."""

    cnn_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cnn_1",
            "id_number",
            "CNN.1",
        ),
        serialization_alias="CNN.1",
        title="ID Number",
    )

    cnn_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cnn_2",
            "family_name",
            "CNN.2",
        ),
        serialization_alias="CNN.2",
        title="Family Name",
    )

    cnn_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cnn_3",
            "given_name",
            "CNN.3",
        ),
        serialization_alias="CNN.3",
        title="Given Name",
    )

    cnn_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cnn_4",
            "second_and_further_given_names_or_initials_thereof",
            "CNN.4",
        ),
        serialization_alias="CNN.4",
        title="Second and Further Given Names or Initials Thereof",
    )

    cnn_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cnn_5",
            "suffix_e_g_jr_or_iii",
            "CNN.5",
        ),
        serialization_alias="CNN.5",
        title="Suffix (e.g., JR or III)",
    )

    cnn_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cnn_6",
            "prefix_e_g_dr",
            "CNN.6",
        ),
        serialization_alias="CNN.6",
        title="Prefix (e.g., DR)",
    )

    cnn_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cnn_7",
            "degree_e_g_md",
            "CNN.7",
        ),
        serialization_alias="CNN.7",
        title="Degree (e.g., MD",
    )

    cnn_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cnn_8",
            "source_table",
            "CNN.8",
        ),
        serialization_alias="CNN.8",
        title="Source Table",
    )

    cnn_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cnn_9",
            "assigning_authority_namespace_id",
            "CNN.9",
        ),
        serialization_alias="CNN.9",
        title="Assigning Authority   - Namespace ID",
    )

    cnn_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cnn_10",
            "assigning_authority_universal_id",
            "CNN.10",
        ),
        serialization_alias="CNN.10",
        title="Assigning Authority  - Universal ID",
    )

    cnn_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cnn_11",
            "assigning_authority_universal_id_type",
            "CNN.11",
        ),
        serialization_alias="CNN.11",
        title="Assigning Authority  - Universal ID Type",
    )

    model_config = {"populate_by_name": True}
