"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: RRE_O12.ENCODING
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.RXC import RXC
from ..segments.RXE import RXE
from ..segments.RXR import RXR
from .RRE_O12_TIMING_ENCODED import RRE_O12_TIMING_ENCODED

_NTE = NTE
_RRE_O12_TIMING_ENCODED = RRE_O12_TIMING_ENCODED
_RXC = RXC
_RXE = RXE
_RXR = RXR


class RRE_O12_ENCODING(BaseModel):
    """HL7 v2 RRE_O12.ENCODING group.

    Attributes:
        RXE (RXE): required
        NTE (Optional[List[NTE]]): optional
        TIMING_ENCODED (List[RRE_O12_TIMING_ENCODED]): required
        RXR (List[RXR]): required
        RXC (Optional[List[RXC]]): optional
    """

    RXE: _RXE = Field(
        default=...,
        title="RXE",
        description="Required",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    TIMING_ENCODED: list[_RRE_O12_TIMING_ENCODED] = Field(
        default=...,
        title="TIMING_ENCODED",
        description="Required, repeating",
    )

    RXR: list[_RXR] = Field(
        default=...,
        title="RXR",
        description="Required, repeating",
    )

    RXC: list[_RXC] | None = Field(
        default=None,
        title="RXC",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
