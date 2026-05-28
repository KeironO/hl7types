"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: CNE
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field


class CNE(BaseModel):
    """HL7 v2 CNE data type."""

    cne_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "cne_1",
            "identifier",
            "CNE.1",
        ),
        serialization_alias="CNE.1",
        title="Identifier",
    )

    cne_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cne_2",
            "text",
            "CNE.2",
        ),
        serialization_alias="CNE.2",
        title="Text",
    )

    cne_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cne_3",
            "name_of_coding_system",
            "CNE.3",
        ),
        serialization_alias="CNE.3",
        title="Name of Coding System",
    )

    cne_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cne_4",
            "alternate_identifier",
            "CNE.4",
        ),
        serialization_alias="CNE.4",
        title="Alternate Identifier",
    )

    cne_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cne_5",
            "alternate_text",
            "CNE.5",
        ),
        serialization_alias="CNE.5",
        title="Alternate Text",
    )

    cne_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cne_6",
            "name_of_alternate_coding_system",
            "CNE.6",
        ),
        serialization_alias="CNE.6",
        title="Name of Alternate Coding System",
    )

    cne_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cne_7",
            "coding_system_version_id",
            "CNE.7",
        ),
        serialization_alias="CNE.7",
        title="Coding System Version ID",
    )

    cne_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cne_8",
            "alternate_coding_system_version_id",
            "CNE.8",
        ),
        serialization_alias="CNE.8",
        title="Alternate Coding System Version ID",
    )

    cne_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cne_9",
            "original_text",
            "CNE.9",
        ),
        serialization_alias="CNE.9",
        title="Original Text",
    )

    model_config = {"populate_by_name": True}
