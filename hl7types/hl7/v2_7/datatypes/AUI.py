"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: AUI
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model


class AUI(HL7Model):
    """HL7 v2 AUI data type.

    Attributes
    ----------
    aui_1 : str | None
        AUI.1 (opt) - Authorization Number (ST)

    aui_2 : str | None
        AUI.2 (opt) - Date (DT)

    aui_3 : str | None
        AUI.3 (opt) - Source (ST)
    """

    aui_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aui_1",
            "authorization_number",
            "AUI.1",
        ),
        serialization_alias="AUI.1",
        title="Authorization Number",
    )

    aui_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aui_2",
            "date",
            "AUI.2",
        ),
        serialization_alias="AUI.2",
        title="Date",
    )

    aui_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aui_3",
            "source",
            "AUI.3",
        ),
        serialization_alias="AUI.3",
        title="Source",
    )

    @field_validator("aui_2", mode='before')
    @classmethod
    def _validate_dt(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\d{4}([01]\d(\d{2})?)?)?', v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 date (YYYY[MM[DD]])")
        return v

    model_config = {"populate_by_name": True}
