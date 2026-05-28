"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: PEX_P07.PEX_OBSERVATION
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.PEO import PEO
from .PEX_P07_PEX_CAUSE import PEX_P07_PEX_CAUSE

_PEO = PEO
_PEX_P07_PEX_CAUSE = PEX_P07_PEX_CAUSE


class PEX_P07_PEX_OBSERVATION(BaseModel):
    """HL7 v2 PEX_P07.PEX_OBSERVATION group.

    Attributes:
        PEO (PEO): required
        PEX_CAUSE (List[PEX_P07_PEX_CAUSE]): required
    """

    PEO: _PEO = Field(
        default=...,
        title="PEO",
        description="Required",
    )

    PEX_CAUSE: list[_PEX_P07_PEX_CAUSE] = Field(
        default=...,
        title="PEX_CAUSE",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
