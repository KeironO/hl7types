"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: RDR_RDR.DISPENSE
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.RXC import RXC
from ..segments.RXD import RXD
from ..segments.RXR import RXR

_RXC = RXC
_RXD = RXD
_RXR = RXR


class RDR_RDR_DISPENSE(BaseModel):
    """HL7 v2 RDR_RDR.DISPENSE group.

    Attributes:
        RXD (RXD): required
        RXR (List[RXR]): required
        RXC (Optional[List[RXC]]): optional
    """

    RXD: _RXD = Field(
        default=...,
        title="RXD",
        description="Required",
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
