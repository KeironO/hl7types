"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: CF
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from .FT import FT


class CF(BaseModel):
    """HL7 v2 CF data type."""

    cf_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cf_1",
            "identifier",
            "CF.1",
        ),
        serialization_alias="CF.1",
        title="identifier",
    )

    cf_2: FT | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cf_2",
            "formatted_text",
            "CF.2",
        ),
        serialization_alias="CF.2",
        title="formatted text",
    )

    cf_3: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cf_3",
            "name_of_coding_system",
            "CF.3",
        ),
        serialization_alias="CF.3",
        title="name of coding system",
    )

    cf_4: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cf_4",
            "alternate_identifier",
            "CF.4",
        ),
        serialization_alias="CF.4",
        title="alternate identifier",
    )

    cf_5: FT | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cf_5",
            "alternate_formatted_text",
            "CF.5",
        ),
        serialization_alias="CF.5",
        title="alternate formatted text",
    )

    cf_6: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cf_6",
            "name_of_alternate_coding_system",
            "CF.6",
        ),
        serialization_alias="CF.6",
        title="name of alternate coding system",
    )

    model_config = {"populate_by_name": True}
