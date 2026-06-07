"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: CSU_C09.RX_ADMIN
Type: Group
"""
from __future__ import annotations

from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.RXA import RXA
from ..segments.RXR import RXR

_RXA = RXA
_RXR = RXR


class CSU_C09_RX_ADMIN(HL7Model):
    """HL7 v2 CSU_C09.RX_ADMIN group.

    Attributes:
        RXA (RXA): required
        RXR (RXR): required
    """

    RXA: _RXA = Field(
        title="RXA",
        description="Required",
    )

    RXR: _RXR = Field(
        title="RXR",
        description="Required",
    )

    model_config = {"populate_by_name": True}
