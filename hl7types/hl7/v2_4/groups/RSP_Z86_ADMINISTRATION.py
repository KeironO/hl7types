"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: RSP_Z86.ADMINISTRATION
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.RXA import RXA
from ..segments.RXC import RXC
from ..segments.RXR import RXR

_RXA = RXA
_RXC = RXC
_RXR = RXR


class RSP_Z86_ADMINISTRATION(HL7Model):
    """HL7 v2 RSP_Z86.ADMINISTRATION group.

    Attributes:
        RXA (RXA): required
        RXR (List[RXR]): required
        RXC (Optional[List[RXC]]): optional
    """

    RXA: _RXA = Field(
        title="RXA",
        description="Required",
    )

    RXR: List[_RXR] = Field(
        min_length=1,
        title="RXR",
        description="Required, repeating",
    )

    RXC: Optional[List[_RXC]] = Field(
        default=None,
        title="RXC",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
