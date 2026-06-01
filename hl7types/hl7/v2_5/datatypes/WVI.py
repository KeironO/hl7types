"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: WVI
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model
from pydantic import field_validator


class WVI(HL7Model):
    """HL7 v2 WVI data type.

    Attributes
    ----------
    wvi_1 : str | None
        WVI.1 (opt) - Channel Number (NM)

    wvi_2 : str | None
        WVI.2 (opt) - Channel Name (ST)
    """

    wvi_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "wvi_1",
            "channel_number",
            "WVI.1",
        ),
        serialization_alias="WVI.1",
        title="Channel Number",
    )

    wvi_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "wvi_2",
            "channel_name",
            "WVI.2",
        ),
        serialization_alias="WVI.2",
        title="Channel Name",
    )

    @field_validator("wvi_1", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
