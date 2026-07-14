"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: RDE_O11.COMPONENT
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


class RDE_O11_COMPONENT(HL7Model):
    """HL7 v2 RDE_O11.COMPONENT group.

    Attributes:
        RXC (RXC): Pharmacy/Treatment Component Order, required
        NTE (Optional[List[NTE]]): Notes and Comments, optional
    """

    RXC: _RXC = Field(
        title="RXC",
        description="Pharmacy/Treatment Component Order",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    model_config = {"populate_by_name": True}
