"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: RSP_K31.ENCODING
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.PRT import PRT
from ..segments.RXC import RXC
from ..segments.RXE import RXE
from ..segments.RXR import RXR

from .RSP_K31_TIMING_ENCODED import RSP_K31_TIMING_ENCODED

_NTE = NTE
_PRT = PRT
_RSP_K31_TIMING_ENCODED = RSP_K31_TIMING_ENCODED
_RXC = RXC
_RXE = RXE
_RXR = RXR


class RSP_K31_ENCODING(BaseModel):
    """HL7 v2 RSP_K31.ENCODING group.

    Attributes:
        RXE (RXE): required
        PRT (Optional[List[PRT]]): optional
        NTE (Optional[List[NTE]]): optional
        TIMING_ENCODED (List[RSP_K31_TIMING_ENCODED]): required
        RXR (List[RXR]): required
        RXC (Optional[List[RXC]]): optional
    """

    RXE: _RXE = Field(
        default=...,
        title="RXE",
        description="Required",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    TIMING_ENCODED: List[_RSP_K31_TIMING_ENCODED] = Field(
        default=...,
        title="TIMING_ENCODED",
        description="Required, repeating",
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
