"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
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
        RXG (RXG): required
        RXR (List[RXR]): required
        RXC (Optional[List[RXC]]): optional
        OBSERVATION (Optional[List[RGV_O01_OBSERVATION]]): optional
    """

    RXG: _RXG = Field(
        default=...,
        title="RXG",
        description="Required",
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

    OBSERVATION: Optional[List[_RGV_O01_OBSERVATION]] = Field(
        default=None,
        title="OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
