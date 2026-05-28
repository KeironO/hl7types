"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: RSP_Z88.ORDER_ENCODED
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.RXC import RXC
from ..segments.RXE import RXE
from ..segments.RXR import RXR

from .RSP_Z88_TIMING_ENCODED import RSP_Z88_TIMING_ENCODED

_RSP_Z88_TIMING_ENCODED = RSP_Z88_TIMING_ENCODED
_RXC = RXC
_RXE = RXE
_RXR = RXR


class RSP_Z88_ORDER_ENCODED(BaseModel):
    """HL7 v2 RSP_Z88.ORDER_ENCODED group.

    Attributes:
        RXE (RXE): required
        TIMING_ENCODED (Optional[List[RSP_Z88_TIMING_ENCODED]]): optional
        RXR (List[RXR]): required
        RXC (Optional[List[RXC]]): optional
    """

    RXE: _RXE = Field(
        default=...,
        title="RXE",
        description="Required",
    )

    TIMING_ENCODED: Optional[List[_RSP_Z88_TIMING_ENCODED]] = Field(
        default=None,
        title="TIMING_ENCODED",
        description="Optional, repeating",
    )

    RXR: List[_RXR] = Field(
        default=...,
        title="RXR",
        description="Required, repeating",
    )

    RXC: Optional[List[_RXC]] = Field(
        default=None,
        title="RXC",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
