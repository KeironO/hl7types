"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: RAS_O01.ENCODING
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.RXC import RXC
from ..segments.RXE import RXE
from ..segments.RXR import RXR

_RXC = RXC
_RXE = RXE
_RXR = RXR


class RAS_O01_ENCODING(HL7Model):
    """HL7 v2 RAS_O01.ENCODING group.

    Attributes:
        RXE (RXE): Pharmacy encoded order segment, required
        RXR (List[RXR]): Pharmacy route segment, required
        RXC (Optional[List[RXC]]): Pharmacy component order segment, optional
    """

    RXE: _RXE = Field(
        title="RXE",
        description="Pharmacy encoded order segment",
    )

    RXR: List[_RXR] = Field(
        min_length=1,
        title="RXR",
        description="Pharmacy route segment",
    )

    RXC: Optional[List[_RXC]] = Field(
        default=None,
        title="RXC",
        description="Pharmacy component order segment",
    )

    model_config = {"populate_by_name": True}
