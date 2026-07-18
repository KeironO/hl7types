"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: ROR_ROR.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.ORC import ORC
from ..segments.RXC import RXC
from ..segments.RXO import RXO
from ..segments.RXR import RXR

_ORC = ORC
_RXC = RXC
_RXO = RXO
_RXR = RXR


class ROR_ROR_ORDER(HL7Model):
    """HL7 v2 ROR_ROR.ORDER group.

    Attributes:
        ORC (ORC): Common Order, required
        RXO (RXO): Pharmacy/Treatment Order, required
        RXR (List[RXR]): Pharmacy/Treatment Route, required
        RXC (Optional[List[RXC]]): Pharmacy/Treatment Component Order, optional
    """

    ORC: _ORC = Field(
        title="ORC",
        description="Common Order",
    )

    RXO: _RXO = Field(
        title="RXO",
        description="Pharmacy/Treatment Order",
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
