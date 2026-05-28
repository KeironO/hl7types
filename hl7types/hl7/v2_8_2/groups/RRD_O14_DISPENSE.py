"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: RRD_O14.DISPENSE
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.RXC import RXC
from ..segments.RXD import RXD
from ..segments.RXR import RXR

_NTE = NTE
_RXC = RXC
_RXD = RXD
_RXR = RXR


class RRD_O14_DISPENSE(BaseModel):
    """HL7 v2 RRD_O14.DISPENSE group.

    Attributes:
        RXD (RXD): required
        NTE (Optional[List[NTE]]): optional
        RXR (List[RXR]): required
        RXC (Optional[List[RXC]]): optional
    """

    RXD: _RXD = Field(
        default=...,
        title="RXD",
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
