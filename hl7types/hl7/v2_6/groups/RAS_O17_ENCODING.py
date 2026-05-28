"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: RAS_O17.ENCODING
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.RXC import RXC
from ..segments.RXE import RXE
from ..segments.RXR import RXR
from .RAS_O17_TIMING_ENCODED import RAS_O17_TIMING_ENCODED

_RAS_O17_TIMING_ENCODED = RAS_O17_TIMING_ENCODED
_RXC = RXC
_RXE = RXE
_RXR = RXR


class RAS_O17_ENCODING(BaseModel):
    """HL7 v2 RAS_O17.ENCODING group.

    Attributes:
        RXE (RXE): required
        TIMING_ENCODED (List[RAS_O17_TIMING_ENCODED]): required
        RXR (List[RXR]): required
        RXC (Optional[List[RXC]]): optional
    """

    RXE: _RXE = Field(
        default=...,
        title="RXE",
        description="Required",
    )

    TIMING_ENCODED: list[_RAS_O17_TIMING_ENCODED] = Field(
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
