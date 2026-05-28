"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: PEX_P07.ASSOCIATED_RX_ORDER
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.RXE import RXE
from ..segments.RXR import RXR

from .PEX_P07_NK1_TIMING_QTY import PEX_P07_NK1_TIMING_QTY

_PEX_P07_NK1_TIMING_QTY = PEX_P07_NK1_TIMING_QTY
_RXE = RXE
_RXR = RXR


class PEX_P07_ASSOCIATED_RX_ORDER(BaseModel):
    """HL7 v2 PEX_P07.ASSOCIATED_RX_ORDER group.

    Attributes:
        RXE (RXE): required
        NK1_TIMING_QTY (List[PEX_P07_NK1_TIMING_QTY]): required
        RXR (Optional[List[RXR]]): optional
    """

    RXE: _RXE = Field(
        default=...,
        title="RXE",
        description="Required",
    )

    NK1_TIMING_QTY: List[_PEX_P07_NK1_TIMING_QTY] = Field(
        default=...,
        title="NK1_TIMING_QTY",
        description="Required, repeating",
    )

    RXR: Optional[List[_RXR]] = Field(
        default=None,
        title="RXR",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
