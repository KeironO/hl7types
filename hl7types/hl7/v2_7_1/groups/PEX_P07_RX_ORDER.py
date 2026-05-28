"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: PEX_P07.RX_ORDER
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.PRT import PRT
from ..segments.RXE import RXE
from ..segments.RXR import RXR
from .PEX_P07_TIMING_QTY import PEX_P07_TIMING_QTY

_PEX_P07_TIMING_QTY = PEX_P07_TIMING_QTY
_PRT = PRT
_RXE = RXE
_RXR = RXR


class PEX_P07_RX_ORDER(BaseModel):
    """HL7 v2 PEX_P07.RX_ORDER group.

    Attributes:
        RXE (RXE): required
        PRT (Optional[List[PRT]]): optional
        TIMING_QTY (List[PEX_P07_TIMING_QTY]): required
        RXR (Optional[List[RXR]]): optional
    """

    RXE: _RXE = Field(
        default=...,
        title="RXE",
        description="Required",
    )

    PRT: list[_PRT] | None = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    TIMING_QTY: list[_PEX_P07_TIMING_QTY] = Field(
        default=...,
        title="TIMING_QTY",
        description="Required, repeating",
    )

    RXR: list[_RXR] | None = Field(
        default=None,
        title="RXR",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
