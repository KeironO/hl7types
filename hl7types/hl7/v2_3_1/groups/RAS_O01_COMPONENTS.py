"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: RAS_O01.COMPONENTS
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


class RAS_O01_COMPONENTS(HL7Model):
    """HL7 v2 RAS_O01.COMPONENTS group.

    Attributes:
        RXC (List[RXC]): RXC - pharmacy/treatment component order segment, required
        NTE (Optional[List[NTE]]): NTE - notes and comments segment, optional
    """

    RXC: List[_RXC] = Field(
        min_length=1,
        title="RXC",
        description="RXC - pharmacy/treatment component order segment",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="NTE - notes and comments segment",
    )

    model_config = ConfigDict(populate_by_name=True)
