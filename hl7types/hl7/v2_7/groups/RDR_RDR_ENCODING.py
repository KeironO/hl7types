"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: RDR_RDR.ENCODING
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.RXC import RXC
from ..segments.RXE import RXE
from ..segments.RXR import RXR

from .RDR_RDR_TIMING_ENCODED import RDR_RDR_TIMING_ENCODED

_RDR_RDR_TIMING_ENCODED = RDR_RDR_TIMING_ENCODED
_RXC = RXC
_RXE = RXE
_RXR = RXR


class RDR_RDR_ENCODING(HL7Model):
    """HL7 v2 RDR_RDR.ENCODING group.

    Attributes:
        RXE (RXE): required
        TIMING_ENCODED (Optional[List[RDR_RDR_TIMING_ENCODED]]): optional
        RXR (List[RXR]): required
        RXC (Optional[List[RXC]]): optional
    """

    RXE: _RXE = Field(
        default=...,
        title="RXE",
        description="Required",
    )

    TIMING_ENCODED: Optional[List[_RDR_RDR_TIMING_ENCODED]] = Field(
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
