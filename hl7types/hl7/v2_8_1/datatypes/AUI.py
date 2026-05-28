"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: AUI
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field


class AUI(BaseModel):
    """HL7 v2 AUI data type."""

    aui_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "aui_1",
            "authorization_number",
            "AUI.1",
        ),
        serialization_alias="AUI.1",
        title="Authorization Number",
    )

    aui_2: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "aui_2",
            "date",
            "AUI.2",
        ),
        serialization_alias="AUI.2",
        title="Date",
    )

    aui_3: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "aui_3",
            "source",
            "AUI.3",
        ),
        serialization_alias="AUI.3",
        title="Source",
    )

    model_config = {"populate_by_name": True}
