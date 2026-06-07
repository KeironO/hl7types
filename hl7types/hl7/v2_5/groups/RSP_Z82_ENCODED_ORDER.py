"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: RSP_Z82.ENCODED_ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.RXC import RXC
from ..segments.RXE import RXE
from ..segments.RXR import RXR

from .RSP_Z82_TIMING_ENCODED import RSP_Z82_TIMING_ENCODED

_RSP_Z82_TIMING_ENCODED = RSP_Z82_TIMING_ENCODED
_RXC = RXC
_RXE = RXE
_RXR = RXR


class RSP_Z82_ENCODED_ORDER(HL7Model):
    """HL7 v2 RSP_Z82.ENCODED_ORDER group.

    Attributes:
        RXE (RXE): required
        TIMING_ENCODED (Optional[List[RSP_Z82_TIMING_ENCODED]]): optional
        RXR (List[RXR]): required
        RXC (Optional[List[RXC]]): optional
    """

    RXE: _RXE = Field(
        title="RXE",
        description="Required",
    )

    TIMING_ENCODED: Optional[List[_RSP_Z82_TIMING_ENCODED]] = Field(
        default=None,
        title="TIMING_ENCODED",
        description="Optional, repeating",
    )

    RXR: List[_RXR] = Field(
        min_length=1,
        title="RXR",
        description="Required, repeating",
    )

    RXC: Optional[List[_RXC]] = Field(
        default=None,
        title="RXC",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
