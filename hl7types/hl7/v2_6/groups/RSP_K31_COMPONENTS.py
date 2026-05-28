"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: RSP_K31.COMPONENTS
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.RXC import RXC

_NTE = NTE
_RXC = RXC


class RSP_K31_COMPONENTS(BaseModel):
    """HL7 v2 RSP_K31.COMPONENTS group.

    Attributes:
        RXC (RXC): required
        NTE (Optional[List[NTE]]): optional
    """

    RXC: _RXC = Field(
        default=...,
        title="RXC",
        description="Required",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
