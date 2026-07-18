"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: RAS_O17.COMPONENTS
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.NTE import NTE
from ..segments.RXC import RXC

_NTE = NTE
_RXC = RXC


class RAS_O17_COMPONENTS(HL7Model):
    """HL7 v2 RAS_O17.COMPONENTS group.

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

    model_config = ConfigDict(populate_by_name=True)
