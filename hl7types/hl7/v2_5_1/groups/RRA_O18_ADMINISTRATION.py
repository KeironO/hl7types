"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: RRA_O18.ADMINISTRATION
Type: Group
"""
from __future__ import annotations

from typing import List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.RXA import RXA
from ..segments.RXR import RXR

_RXA = RXA
_RXR = RXR


class RRA_O18_ADMINISTRATION(HL7Model):
    """HL7 v2 RRA_O18.ADMINISTRATION group.

    Attributes:
        RXA (List[RXA]): Pharmacy/Treatment Administration, required
        RXR (RXR): Pharmacy/Treatment Route, required
    """

    RXA: List[_RXA] = Field(
        min_length=1,
        title="RXA",
        description="Pharmacy/Treatment Administration",
    )

    RXR: _RXR = Field(
        title="RXR",
        description="Pharmacy/Treatment Route",
    )

    model_config = ConfigDict(populate_by_name=True)
