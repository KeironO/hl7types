"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: PEX_P07.ASSOCIATED_RX_ADMIN
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.RXA import RXA
from ..segments.RXR import RXR

_RXA = RXA
_RXR = RXR


class PEX_P07_ASSOCIATED_RX_ADMIN(HL7Model):
    """HL7 v2 PEX_P07.ASSOCIATED_RX_ADMIN group.

    Attributes:
        RXA (RXA): required
        RXR (Optional[RXR]): optional
    """

    RXA: _RXA = Field(
        title="RXA",
        description="Required",
    )

    RXR: Optional[_RXR] = Field(
        default=None,
        title="RXR",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
