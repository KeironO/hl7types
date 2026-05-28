"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: RRA_O02.ADMINISTRATION
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.RXA import RXA
from ..segments.RXR import RXR

_RXA = RXA
_RXR = RXR


class RRA_O02_ADMINISTRATION(BaseModel):
    """HL7 v2 RRA_O02.ADMINISTRATION group.

    Attributes:
        RXA (RXA): required
        RXR (RXR): required
    """

    RXA: _RXA = Field(
        default=...,
        title="RXA",
        description="Required",
    )

    RXR: _RXR = Field(
        default=...,
        title="RXR",
        description="Required",
    )

    model_config = {"populate_by_name": True}
