"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: RRO_O02.ORDER_DETAIL
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.RXC import RXC
from ..segments.RXO import RXO
from ..segments.RXR import RXR

_NTE = NTE
_RXC = RXC
_RXO = RXO
_RXR = RXR


class RRO_O02_ORDER_DETAIL(BaseModel):
    """HL7 v2 RRO_O02.ORDER_DETAIL group.

    Attributes:
        RXO (RXO): required
        NTE (Optional[List[NTE]]): optional
        RXR (List[RXR]): required
        RXC (Optional[List[RXC]]): optional
    """

    RXO: _RXO = Field(
        default=...,
        title="RXO",
        description="Required",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
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

    model_config = {"populate_by_name": True}
