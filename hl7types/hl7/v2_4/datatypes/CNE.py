"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: CNE
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field


class CNE(BaseModel):
    """HL7 v2 CNE data type."""

    cne_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cne_1",
            "identifier_st",
            "CNE.1",
        ),
        serialization_alias="CNE.1",
        title="identifier (ST)",
    )

    cne_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cne_2",
            "text",
            "CNE.2",
        ),
        serialization_alias="CNE.2",
        title="text",
    )

    cne_3: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cne_3",
            "name_of_coding_system",
            "CNE.3",
        ),
        serialization_alias="CNE.3",
        title="name of coding system",
    )

    cne_4: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cne_4",
            "alternate_identifier_st",
            "CNE.4",
        ),
        serialization_alias="CNE.4",
        title="alternate identifier (ST)",
    )

    cne_5: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cne_5",
            "alternate_text",
            "CNE.5",
        ),
        serialization_alias="CNE.5",
        title="alternate text",
    )

    cne_6: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cne_6",
            "name_of_alternate_coding_system",
            "CNE.6",
        ),
        serialization_alias="CNE.6",
        title="name of alternate coding system",
    )

    cne_7: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cne_7",
            "coding_system_version_id",
            "CNE.7",
        ),
        serialization_alias="CNE.7",
        title="coding system version ID",
    )

    cne_8: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cne_8",
            "alternate_coding_system_version_id",
            "CNE.8",
        ),
        serialization_alias="CNE.8",
        title="alternate coding system version ID",
    )

    cne_9: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cne_9",
            "original_text",
            "CNE.9",
        ),
        serialization_alias="CNE.9",
        title="original text",
    )

    model_config = {"populate_by_name": True}
