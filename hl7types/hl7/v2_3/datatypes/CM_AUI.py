"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: CM_AUI
Type: Datatype
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from .TS import TS


class CM_AUI(BaseModel):
    """HL7 v2 CM_AUI data type."""

    cm_aui_1: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_aui_1",
            "authorization_number",
            "CM_AUI.1",
        ),
        serialization_alias="CM_AUI.1",
        title="authorization number",
    )

    cm_aui_2: TS | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_aui_2",
            "date",
            "CM_AUI.2",
        ),
        serialization_alias="CM_AUI.2",
        title="date",
    )

    cm_aui_3: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_aui_3",
            "source",
            "CM_AUI.3",
        ),
        serialization_alias="CM_AUI.3",
        title="source",
    )

    model_config = {"populate_by_name": True}
