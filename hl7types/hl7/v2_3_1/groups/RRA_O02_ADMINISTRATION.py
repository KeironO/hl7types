"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: RRA_O02.ADMINISTRATION
Type: Group
"""
from __future__ import annotations

from typing import List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.RXA import RXA
from ..segments.RXR import RXR

_RXA = RXA
_RXR = RXR


class RRA_O02_ADMINISTRATION(HL7Model):
    """HL7 v2 RRA_O02.ADMINISTRATION group.

    Attributes:
        RXA (List[RXA]): RXA - pharmacy/treatment administration segment, required
        RXR (RXR): RXR - pharmacy/treatment route segment, required
    """

    RXA: List[_RXA] = Field(
        min_length=1,
        title="RXA",
        description="RXA - pharmacy/treatment administration segment",
    )

    RXR: _RXR = Field(
        title="RXR",
        description="RXR - pharmacy/treatment route segment",
    )

    model_config = {"populate_by_name": True}
