"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: PEX_P07.ASSOCIATED_RX_ADMIN
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.RXA import RXA
from ..segments.RXR import RXR

_RXA = RXA
_RXR = RXR


class PEX_P07_ASSOCIATED_RX_ADMIN(HL7Model):
    """HL7 v2 PEX_P07.ASSOCIATED_RX_ADMIN group.

    Attributes:
        RXA (RXA): RXA - pharmacy/treatment administration segment, required
        RXR (Optional[RXR]): RXR - pharmacy/treatment route segment, optional
    """

    RXA: _RXA = Field(
        title="RXA",
        description="RXA - pharmacy/treatment administration segment",
    )

    RXR: Optional[_RXR] = Field(
        default=None,
        title="RXR",
        description="RXR - pharmacy/treatment route segment",
    )

    model_config = ConfigDict(populate_by_name=True)
