"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: RGV_O15.GIVE
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.RXC import RXC
from ..segments.RXG import RXG
from ..segments.RXR import RXR

from .RGV_O15_OBSERVATION import RGV_O15_OBSERVATION

_RGV_O15_OBSERVATION = RGV_O15_OBSERVATION
_RXC = RXC
_RXG = RXG
_RXR = RXR


class RGV_O15_GIVE(HL7Model):
    """HL7 v2 RGV_O15.GIVE group.

    Attributes:
        RXG (RXG): required
        RXR (List[RXR]): required
        RXC (Optional[List[RXC]]): optional
        OBSERVATION (List[RGV_O15_OBSERVATION]): required
    """

    RXG: _RXG = Field(
        title="RXG",
        description="Required",
    )

    RXR: List[_RXR] = Field(
        min_length=1,
        title="RXR",
        description="Required, repeating",
    )

    RXC: Optional[List[_RXC]] = Field(
        default=None,
        title="RXC",
        description="Optional, repeating",
    )

    OBSERVATION: List[_RGV_O15_OBSERVATION] = Field(
        min_length=1,
        title="OBSERVATION",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
