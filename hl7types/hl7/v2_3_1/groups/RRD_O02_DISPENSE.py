"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: RRD_O02.DISPENSE
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.RXC import RXC
from ..segments.RXD import RXD
from ..segments.RXR import RXR

_RXC = RXC
_RXD = RXD
_RXR = RXR


class RRD_O02_DISPENSE(HL7Model):
    """HL7 v2 RRD_O02.DISPENSE group.

    Attributes:
        RXD (RXD): RXD - pharmacy/treatment dispense segment, required
        RXR (List[RXR]): RXR - pharmacy/treatment route segment, required
        RXC (Optional[List[RXC]]): RXC - pharmacy/treatment component order segment, optional
    """

    RXD: _RXD = Field(
        title="RXD",
        description="RXD - pharmacy/treatment dispense segment",
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

    model_config = ConfigDict(populate_by_name=True)
