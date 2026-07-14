"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: RRO_O02.ORDER_DETAIL
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


class RRO_O02_ORDER_DETAIL(HL7Model):
    """HL7 v2 RRO_O02.ORDER_DETAIL group.

    Attributes:
        RXO (RXO): Pharmacy prescription order segment, required
        NTE (Optional[List[NTE]]): Notes and comments segment, optional
        RXR (List[RXR]): Pharmacy route segment, required
        RXC (Optional[List[RXC]]): Pharmacy component order segment, optional
    """

    RXO: _RXO = Field(
        title="RXO",
        description="Pharmacy prescription order segment",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and comments segment",
    )

    RXR: List[_RXR] = Field(
        min_length=1,
        title="RXR",
        description="Pharmacy route segment",
    )

    RXC: Optional[List[_RXC]] = Field(
        default=None,
        title="RXC",
        description="Pharmacy component order segment",
    )

    model_config = {"populate_by_name": True}
