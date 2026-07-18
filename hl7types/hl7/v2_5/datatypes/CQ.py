"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: CQ
Type: Datatype
"""
from __future__ import annotations

import re

from typing import Optional
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from .CE import CE

_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class CQ(HL7Model):
    """Composite quantity with units (S2.A.11).

    Attributes
    ----------
    cq_1 : str | None
        CQ.1 (opt) - Quantity (NM)

    cq_2 : CE | None
        CQ.2 (opt) - Units (CE)
    """

    cq_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cq_1",
            "quantity",
            "CQ.1",
        ),
        serialization_alias="CQ.1",
        title="Quantity",
    )

    cq_2: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "cq_2",
            "units",
            "CQ.2",
        ),
        serialization_alias="CQ.2",
        title="Units",
    )

    @field_validator("cq_1", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
