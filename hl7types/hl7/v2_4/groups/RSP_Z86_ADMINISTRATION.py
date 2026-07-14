"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: RSP_Z86.ADMINISTRATION
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.RXA import RXA
from ..segments.RXC import RXC
from ..segments.RXR import RXR

_RXA = RXA
_RXC = RXC
_RXR = RXR


class RSP_Z86_ADMINISTRATION(HL7Model):
    """HL7 v2 RSP_Z86.ADMINISTRATION group.

    Attributes:
        RXA (RXA): Pharmacy/Treatment Administration, required
        RXR (List[RXR]): Pharmacy/Treatment Route, required
        RXC (Optional[List[RXC]]): Pharmacy/Treatment Component Order, optional
    """

    RXA: _RXA = Field(
        title="RXA",
        description="Pharmacy/Treatment Administration",
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

    model_config = {"populate_by_name": True}
