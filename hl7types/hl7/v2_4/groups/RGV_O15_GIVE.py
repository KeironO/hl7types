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
        RXG (RXG): Pharmacy/Treatment Give, required
        RXR (List[RXR]): Pharmacy/Treatment Route, required
        RXC (Optional[List[RXC]]): Pharmacy/Treatment Component Order, optional
        OBSERVATION (List[RGV_O15_OBSERVATION]): required
    """

    RXG: _RXG = Field(
        title="RXG",
        description="Pharmacy/Treatment Give",
    )

    RXR: List[_RXR] = Field(
        min_length=1,
        title="RXR",
        description="Pharmacy/Treatment Route",
    )

    RXC: Optional[List[_RXC]] = Field(
        default=None,
        title="RXC",
        description="Pharmacy/Treatment Component Order",
    )

    OBSERVATION: List[_RGV_O15_OBSERVATION] = Field(
        min_length=1,
        title="OBSERVATION",
    )

    model_config = {"populate_by_name": True}
