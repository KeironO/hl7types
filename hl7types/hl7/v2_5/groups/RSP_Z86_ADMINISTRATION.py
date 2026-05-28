"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: RSP_Z86.ADMINISTRATION
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.RXA import RXA
from ..segments.RXC import RXC
from ..segments.RXR import RXR

_RXA = RXA
_RXC = RXC
_RXR = RXR


class RSP_Z86_ADMINISTRATION(BaseModel):
    """HL7 v2 RSP_Z86.ADMINISTRATION group.

    Attributes:
        RXA (RXA): required
        RXR (List[RXR]): required
        RXC (Optional[List[RXC]]): optional
    """

    RXA: _RXA = Field(
        default=...,
        title="RXA",
        description="Required",
    )

    RXR: list[_RXR] = Field(
        default=...,
        title="RXR",
        description="Required, repeating",
    )

    RXC: list[_RXC] | None = Field(
        default=None,
        title="RXC",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
