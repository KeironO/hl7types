"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: CM_WVI
Type: Datatype
"""
from __future__ import annotations

import re

from typing import Optional
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class CM_WVI(HL7Model):
    """Channel identifier.

    Attributes
    ----------
    cm_wvi_1 : str | None
        CM_WVI.1 (opt) - Channel Number (NM)

    cm_wvi_2 : str | None
        CM_WVI.2 (opt) - Channel Name (ST)
    """

    cm_wvi_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_wvi_1",
            "channel_number",
            "CM_WVI.1",
        ),
        serialization_alias="CM_WVI.1",
        title="Channel Number",
    )

    cm_wvi_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_wvi_2",
            "channel_name",
            "CM_WVI.2",
        ),
        serialization_alias="CM_WVI.2",
        title="Channel Name",
    )

    @field_validator("cm_wvi_1", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
