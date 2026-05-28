"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: PEX_P07.RX_ADMINISTRATION
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.RXA import RXA
from ..segments.RXR import RXR

_RXA = RXA
_RXR = RXR


class PEX_P07_RX_ADMINISTRATION(BaseModel):
    """HL7 v2 PEX_P07.RX_ADMINISTRATION group.

    Attributes:
        RXA (RXA): required
        RXR (Optional[RXR]): optional
    """

    RXA: _RXA = Field(
        default=...,
        title="RXA",
        description="Required",
    )

    RXR: _RXR | None = Field(
        default=None,
        title="RXR",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
