"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: RRA_O02.ADMINISTRATION
Type: Group
"""
from __future__ import annotations

from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.RXA import RXA
from ..segments.RXR import RXR

_RXA = RXA
_RXR = RXR


class RRA_O02_ADMINISTRATION(HL7Model):
    """HL7 v2 RRA_O02.ADMINISTRATION group.

    Attributes:
        RXA (RXA): Pharmacy administration segment, required
        RXR (RXR): Pharmacy route segment, required
    """

    RXA: _RXA = Field(
        title="RXA",
        description="Pharmacy administration segment",
    )

    RXR: _RXR = Field(
        title="RXR",
        description="Pharmacy route segment",
    )

    model_config = ConfigDict(populate_by_name=True)
