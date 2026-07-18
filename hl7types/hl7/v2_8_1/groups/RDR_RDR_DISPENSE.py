"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: RDR_RDR.DISPENSE
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


class RDR_RDR_DISPENSE(HL7Model):
    """HL7 v2 RDR_RDR.DISPENSE group.

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

    model_config = ConfigDict(populate_by_name=True)
