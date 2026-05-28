"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: RDS_O13.COMPONENT
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.RXC import RXC

_NTE = NTE
_RXC = RXC


class RDS_O13_COMPONENT(BaseModel):
    """HL7 v2 RDS_O13.COMPONENT group.

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
