"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: RAS_O17.ENCODING
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.RXC import RXC
from ..segments.RXE import RXE
from ..segments.RXR import RXR

from .RAS_O17_TIMING_ENCODED import RAS_O17_TIMING_ENCODED

_RAS_O17_TIMING_ENCODED = RAS_O17_TIMING_ENCODED
_RXC = RXC
_RXE = RXE
_RXR = RXR


class RAS_O17_ENCODING(HL7Model):
    """HL7 v2 RAS_O17.ENCODING group.

    Attributes:
        RXE (RXE): Pharmacy/Treatment Encoded Order, required
        TIMING_ENCODED (List[RAS_O17_TIMING_ENCODED]): required
        RXR (List[RXR]): Pharmacy/Treatment Route, required
        RXC (Optional[List[RXC]]): Pharmacy/Treatment Component Order, optional
    """

    RXE: _RXE = Field(
        title="RXE",
        description="Pharmacy/Treatment Encoded Order",
    )

    TIMING_ENCODED: List[_RAS_O17_TIMING_ENCODED] = Field(
        min_length=1,
        title="TIMING_ENCODED",
    )

    RXR: List[_RXR] = Field(
        min_length=1,
        title="RXR",
        description="Pharmacy/Treatment Route",
    )

    RXC: Optional[List[_RXC]] = Field(
        default=None,
        title="RXC",
        description="Pharmacy/Treatment Component Order",
    )

    model_config = {"populate_by_name": True}
