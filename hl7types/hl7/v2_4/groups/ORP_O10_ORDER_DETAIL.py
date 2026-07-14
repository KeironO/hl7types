"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: ORP_O10.ORDER_DETAIL
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.RXC import RXC
from ..segments.RXO import RXO
from ..segments.RXR import RXR

_NTE = NTE
_RXC = RXC
_RXO = RXO
_RXR = RXR


class ORP_O10_ORDER_DETAIL(HL7Model):
    """HL7 v2 ORP_O10.ORDER_DETAIL group.

    Attributes:
        RXO (RXO): Pharmacy/Treatment Order, required
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        RXR (List[RXR]): Pharmacy/Treatment Route, required
        RXC (Optional[List[RXC]]): Pharmacy/Treatment Component Order, optional
    """

    RXO: _RXO = Field(
        title="RXO",
        description="Pharmacy/Treatment Order",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
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
