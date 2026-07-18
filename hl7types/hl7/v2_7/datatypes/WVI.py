"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: WVI
Type: Datatype
"""
from __future__ import annotations

import re

from typing import Optional
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class WVI(HL7Model):
    """Channel identifier (S2.A.84).

    Attributes
    ----------
    wvi_1 : str
        WVI.1 (req) - Channel Number (NM)

    wvi_2 : str | None
        WVI.2 (opt) - Channel Name (ST)
    """

    wvi_1: str = Field(
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
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
