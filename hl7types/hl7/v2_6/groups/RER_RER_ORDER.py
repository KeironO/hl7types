"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: RER_RER.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.ORC import ORC
from ..segments.RXC import RXC
from ..segments.RXE import RXE
from ..segments.RXR import RXR

_ORC = ORC
_RXC = RXC
_RXE = RXE
_RXR = RXR


class RER_RER_ORDER(HL7Model):
    """HL7 v2 RER_RER.ORDER group.

    Attributes:
        ORC (ORC): Common Order, required
        RXE (RXE): Pharmacy/Treatment Encoded Order, required
        RXR (List[RXR]): Pharmacy/Treatment Route, required
        RXC (Optional[List[RXC]]): Pharmacy/Treatment Component Order, optional
    """

    ORC: _ORC = Field(
        title="ORC",
        description="Common Order",
    )

    RXE: _RXE = Field(
        title="RXE",
        description="Pharmacy/Treatment Encoded Order",
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
