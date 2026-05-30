"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: RDS_O13.COMPONENT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.RXC import RXC

_NTE = NTE
_RXC = RXC


class RDS_O13_COMPONENT(HL7Model):
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

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
