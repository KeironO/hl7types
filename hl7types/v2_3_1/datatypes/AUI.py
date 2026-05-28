"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: AUI
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, BaseModel, Field

from .TS import TS


class AUI(BaseModel):
    """HL7 v2 AUI data type."""

    aui_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aui_1",
            "authorization_number",
            "AUI.1",
        ),
        serialization_alias="AUI.1",
        title="authorization number",
    )

    aui_2: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aui_2",
            "date",
            "AUI.2",
        ),
        serialization_alias="AUI.2",
        title="date",
    )

    aui_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aui_3",
            "source",
            "AUI.3",
        ),
        serialization_alias="AUI.3",
        title="source",
    )

    model_config = {"populate_by_name": True}
