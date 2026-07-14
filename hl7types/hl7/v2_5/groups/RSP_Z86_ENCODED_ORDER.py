"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: RSP_Z86.ENCODED_ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.RXC import RXC
from ..segments.RXE import RXE
from ..segments.RXR import RXR

from .RSP_Z86_TIMING_ENCODED import RSP_Z86_TIMING_ENCODED

_RSP_Z86_TIMING_ENCODED = RSP_Z86_TIMING_ENCODED
_RXC = RXC
_RXE = RXE
_RXR = RXR


class RSP_Z86_ENCODED_ORDER(HL7Model):
    """HL7 v2 RSP_Z86.ENCODED_ORDER group.

    Attributes:
        RXE (RXE): Pharmacy/Treatment Encoded Order, required
        TIMING_ENCODED (Optional[List[RSP_Z86_TIMING_ENCODED]]): optional
        RXR (List[RXR]): Pharmacy/Treatment Route, required
        RXC (Optional[List[RXC]]): Pharmacy/Treatment Component Order, optional
    """

    RXE: _RXE = Field(
        title="RXE",
        description="Pharmacy/Treatment Encoded Order",
    )

    TIMING_ENCODED: Optional[List[_RSP_Z86_TIMING_ENCODED]] = Field(
        default=None,
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
