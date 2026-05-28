"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: FN
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field


class FN(BaseModel):
    """HL7 v2 FN data type."""

    fn_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "fn_1",
            "surname",
            "FN.1",
        ),
        serialization_alias="FN.1",
        title="Surname",
    )

    fn_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "fn_2",
            "own_surname_prefix",
            "FN.2",
        ),
        serialization_alias="FN.2",
        title="Own Surname Prefix",
    )

    fn_3: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "fn_3",
            "own_surname",
            "FN.3",
        ),
        serialization_alias="FN.3",
        title="Own Surname",
    )

    fn_4: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "fn_4",
            "surname_prefix_from_partner_spouse",
            "FN.4",
        ),
        serialization_alias="FN.4",
        title="Surname Prefix from Partner/Spouse",
    )

    fn_5: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "fn_5",
            "surname_from_partner_spouse",
            "FN.5",
        ),
        serialization_alias="FN.5",
        title="Surname from Partner/Spouse",
    )

    model_config = {"populate_by_name": True}
