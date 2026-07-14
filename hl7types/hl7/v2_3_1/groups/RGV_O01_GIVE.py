"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: RGV_O01.GIVE
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.RXC import RXC
from ..segments.RXG import RXG
from ..segments.RXR import RXR

from .RGV_O01_OBSERVATION import RGV_O01_OBSERVATION

_RGV_O01_OBSERVATION = RGV_O01_OBSERVATION
_RXC = RXC
_RXG = RXG
_RXR = RXR


class RGV_O01_GIVE(HL7Model):
    """HL7 v2 RGV_O01.GIVE group.

    Attributes:
        RXG (RXG): RXG - pharmacy/treatment give segment, required
        RXR (List[RXR]): RXR - pharmacy/treatment route segment, required
        RXC (Optional[List[RXC]]): RXC - pharmacy/treatment component order segment, optional
        OBSERVATION (List[RGV_O01_OBSERVATION]): required
    """

    RXG: _RXG = Field(
        title="RXG",
        description="RXG - pharmacy/treatment give segment",
    )

    RXR: List[_RXR] = Field(
        min_length=1,
        title="RXR",
        description="RXR - pharmacy/treatment route segment",
    )

    RXC: Optional[List[_RXC]] = Field(
        default=None,
        title="RXC",
        description="RXC - pharmacy/treatment component order segment",
    )

    OBSERVATION: List[_RGV_O01_OBSERVATION] = Field(
        min_length=1,
        title="OBSERVATION",
    )

    model_config = {"populate_by_name": True}
