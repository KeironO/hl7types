"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: RRG_O16.GIVE
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.RXC import RXC
from ..segments.RXG import RXG
from ..segments.RXR import RXR

_RXC = RXC
_RXG = RXG
_RXR = RXR


class RRG_O16_GIVE(HL7Model):
    """HL7 v2 RRG_O16.GIVE group.

    Attributes:
        RXG (RXG): required
        RXR (List[RXR]): required
        RXC (Optional[List[RXC]]): optional
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

    model_config = {"populate_by_name": True}
