"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: RDE_O01.COMPONENT
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


class RDE_O01_COMPONENT(HL7Model):
    """HL7 v2 RDE_O01.COMPONENT group.

    Attributes:
        RXC (List[RXC]): Pharmacy component order segment, required
        NTE (Optional[List[NTE]]): Notes and comments segment, optional
    """

    RXC: List[_RXC] = Field(
        min_length=1,
        title="RXC",
        description="Pharmacy component order segment",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and comments segment",
    )

    model_config = ConfigDict(populate_by_name=True)
