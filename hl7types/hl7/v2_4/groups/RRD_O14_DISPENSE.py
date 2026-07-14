"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: RRD_O14.DISPENSE
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.RXC import RXC
from ..segments.RXD import RXD
from ..segments.RXR import RXR

_RXC = RXC
_RXD = RXD
_RXR = RXR


class RRD_O14_DISPENSE(HL7Model):
    """HL7 v2 RRD_O14.DISPENSE group.

    Attributes:
        RXD (RXD): Pharmacy/Treatment Dispense, required
        RXR (List[RXR]): Pharmacy/Treatment Route, required
        RXC (Optional[List[RXC]]): Pharmacy/Treatment Component Order, optional
    """

    RXD: _RXD = Field(
        title="RXD",
        description="Pharmacy/Treatment Dispense",
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
