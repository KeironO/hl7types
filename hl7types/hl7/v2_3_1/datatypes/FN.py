"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: FN
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field


class FN(BaseModel):
    """HL7 v2 FN data type."""

    fn_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "fn_1",
            "family_name",
            "FN.1",
        ),
        serialization_alias="FN.1",
        title="family name",
    )

    fn_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "fn_2",
            "last_name_prefix",
            "FN.2",
        ),
        serialization_alias="FN.2",
        title="last name prefix",
    )

    model_config = {"populate_by_name": True}
