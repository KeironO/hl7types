"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: RRG_O16.GIVE
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.RXC import RXC
from ..segments.RXG import RXG
from ..segments.RXR import RXR

from .RRG_O16_TIMING_GIVE import RRG_O16_TIMING_GIVE

_RRG_O16_TIMING_GIVE = RRG_O16_TIMING_GIVE
_RXC = RXC
_RXG = RXG
_RXR = RXR


class RRG_O16_GIVE(BaseModel):
    """HL7 v2 RRG_O16.GIVE group.

    Attributes:
        RXG (RXG): required
        TIMING_GIVE (List[RRG_O16_TIMING_GIVE]): required
        RXR (List[RXR]): required
        RXC (Optional[List[RXC]]): optional
    """

    RXG: _RXG = Field(
        default=...,
        title="RXG",
        description="Required",
    )

    TIMING_GIVE: List[_RRG_O16_TIMING_GIVE] = Field(
        default=...,
        title="TIMING_GIVE",
        description="Required, repeating",
    )

    RXR: List[_RXR] = Field(
        default=...,
        title="RXR",
        description="Required, repeating",
    )

    RXC: Optional[List[_RXC]] = Field(
        default=None,
        title="RXC",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
