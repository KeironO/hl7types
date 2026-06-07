"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: RSP_Z88.COMPONENT
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


class RSP_Z88_COMPONENT(HL7Model):
    """HL7 v2 RSP_Z88.COMPONENT group.

    Attributes:
        RXC (List[RXC]): required
        NTE (Optional[List[NTE]]): optional
    """

    RXC: List[_RXC] = Field(
        min_length=1,
        title="RXC",
        description="Required, repeating",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
