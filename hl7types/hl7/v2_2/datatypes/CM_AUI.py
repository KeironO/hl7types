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
from pydantic import field_validator


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

    @field_validator("cm_aui_2", mode='before')
    @classmethod
    def _validate_dt(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\d{4}([01]\d(\d{2})?)?)?', v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 date (YYYY[MM[DD]])")
        return v

    model_config = {"populate_by_name": True}
