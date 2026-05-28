"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: RRA_O18.ADMINISTRATION
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.RXA import RXA
from ..segments.RXR import RXR

_RXA = RXA
_RXR = RXR


class RRA_O18_ADMINISTRATION(BaseModel):
    """HL7 v2 RRA_O18.ADMINISTRATION group.

    Attributes:
        RXA (List[RXA]): required
        RXR (RXR): required
    """

    RXA: list[_RXA] = Field(
        default=...,
        title="RXA",
        description="Required, repeating",
    )

    RXR: _RXR = Field(
        default=...,
        title="RXR",
        description="Required",
    )

    model_config = {"populate_by_name": True}
