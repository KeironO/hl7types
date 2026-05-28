"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: PEX_P07.EXPERIENCE
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.PES import PES

from .PEX_P07_PEX_OBSERVATION import PEX_P07_PEX_OBSERVATION

_PES = PES
_PEX_P07_PEX_OBSERVATION = PEX_P07_PEX_OBSERVATION


class PEX_P07_EXPERIENCE(BaseModel):
    """HL7 v2 PEX_P07.EXPERIENCE group.

    Attributes:
        PES (PES): required
        PEX_OBSERVATION (List[PEX_P07_PEX_OBSERVATION]): required
    """

    PES: _PES = Field(
        default=...,
        title="PES",
        description="Required",
    )

    PEX_OBSERVATION: List[_PEX_P07_PEX_OBSERVATION] = Field(
        default=...,
        title="PEX_OBSERVATION",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
