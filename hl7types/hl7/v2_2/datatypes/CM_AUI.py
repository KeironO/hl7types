"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: CM_AUI
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model


class CM_AUI(HL7Model):
    """HL7 v2 CM_AUI data type.

    Attributes
    ----------
    cm_aui_1 : str | None
        CM_AUI.1 (opt) - authorization number (ST)

    cm_aui_2 : str | None
        CM_AUI.2 (opt) - date (DT)

    cm_aui_3 : str | None
        CM_AUI.3 (opt) - source (ST)
    """

    cm_aui_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_aui_1",
            "authorization_number",
            "CM_AUI.1",
        ),
        serialization_alias="CM_AUI.1",
        title="authorization number",
    )

    cm_aui_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_aui_2",
            "date",
            "CM_AUI.2",
        ),
        serialization_alias="CM_AUI.2",
        title="date",
    )

    cm_aui_3: Optional[str] = Field(
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
