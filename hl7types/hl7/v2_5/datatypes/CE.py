"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: CE
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field


class CE(BaseModel):
    """HL7 v2 CE data type."""

    ce_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ce_1",
            "identifier",
            "CE.1",
        ),
        serialization_alias="CE.1",
        title="Identifier",
    )

    ce_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ce_2",
            "text",
            "CE.2",
        ),
        serialization_alias="CE.2",
        title="Text",
    )

    ce_3: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ce_3",
            "name_of_coding_system",
            "CE.3",
        ),
        serialization_alias="CE.3",
        title="Name of Coding System",
    )

    ce_4: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ce_4",
            "alternate_identifier",
            "CE.4",
        ),
        serialization_alias="CE.4",
        title="Alternate Identifier",
    )

    ce_5: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ce_5",
            "alternate_text",
            "CE.5",
        ),
        serialization_alias="CE.5",
        title="Alternate Text",
    )

    ce_6: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "ce_6",
            "name_of_alternate_coding_system",
            "CE.6",
        ),
        serialization_alias="CE.6",
        title="Name of Alternate Coding System",
    )

    model_config = {"populate_by_name": True}
