"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: RGV_O15.GIVE
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.CDO import CDO
from ..segments.RXC import RXC
from ..segments.RXG import RXG
from ..segments.RXR import RXR
from .RGV_O15_OBSERVATION import RGV_O15_OBSERVATION
from .RGV_O15_TIMING_GIVE import RGV_O15_TIMING_GIVE

_CDO = CDO
_RGV_O15_OBSERVATION = RGV_O15_OBSERVATION
_RGV_O15_TIMING_GIVE = RGV_O15_TIMING_GIVE
_RXC = RXC
_RXG = RXG
_RXR = RXR


class RGV_O15_GIVE(BaseModel):
    """HL7 v2 RGV_O15.GIVE group.

    Attributes:
        RXG (RXG): required
        TIMING_GIVE (List[RGV_O15_TIMING_GIVE]): required
        RXR (List[RXR]): required
        RXC (Optional[List[RXC]]): optional
        CDO (Optional[List[CDO]]): optional
        OBSERVATION (Optional[List[RGV_O15_OBSERVATION]]): optional
    """

    RXG: _RXG = Field(
        default=...,
        title="RXG",
        description="Required",
    )

    TIMING_GIVE: list[_RGV_O15_TIMING_GIVE] = Field(
        default=...,
        title="TIMING_GIVE",
        description="Required, repeating",
    )

    RXR: list[_RXR] = Field(
        default=...,
        title="RXR",
        description="Required, repeating",
    )

    RXC: list[_RXC] | None = Field(
        default=None,
        title="RXC",
        description="Optional, repeating",
    )

    CDO: list[_CDO] | None = Field(
        default=None,
        title="CDO",
        description="Optional, repeating",
    )

    OBSERVATION: list[_RGV_O15_OBSERVATION] | None = Field(
        default=None,
        title="OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
