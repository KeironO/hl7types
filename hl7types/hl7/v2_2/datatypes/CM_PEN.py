"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: CM_PEN
Type: Datatype
"""
from __future__ import annotations

import re

from typing import Optional
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class CM_PEN(HL7Model):
    """Penalty.

    Attributes
    ----------
    cm_pen_1 : str | None
        CM_PEN.1 (opt) - Penalty ID (ID)

    cm_pen_2 : str | None
        CM_PEN.2 (opt) - penalty amount (NM)
    """

    cm_pen_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_pen_1",
            "penalty_id",
            "CM_PEN.1",
        ),
        serialization_alias="CM_PEN.1",
        title="Penalty ID",
    )

    cm_pen_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cm_pen_2",
            "penalty_amount",
            "CM_PEN.2",
        ),
        serialization_alias="CM_PEN.2",
        title="penalty amount",
    )

    @field_validator("cm_pen_2", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
