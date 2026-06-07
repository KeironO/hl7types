"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: PEX_P07.ASSOCIATED_RX_ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.PRT import PRT
from ..segments.RXE import RXE
from ..segments.RXR import RXR

from .PEX_P07_NK1_TIMING_QTY import PEX_P07_NK1_TIMING_QTY

_PEX_P07_NK1_TIMING_QTY = PEX_P07_NK1_TIMING_QTY
_PRT = PRT
_RXE = RXE
_RXR = RXR


class PEX_P07_ASSOCIATED_RX_ORDER(HL7Model):
    """HL7 v2 PEX_P07.ASSOCIATED_RX_ORDER group.

    Attributes:
        RXE (RXE): required
        PRT (Optional[List[PRT]]): optional
        NK1_TIMING_QTY (List[PEX_P07_NK1_TIMING_QTY]): required
        RXR (Optional[List[RXR]]): optional
    """

    RXE: _RXE = Field(
        title="RXE",
        description="Required",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    NK1_TIMING_QTY: List[_PEX_P07_NK1_TIMING_QTY] = Field(
        min_length=1,
        title="NK1_TIMING_QTY",
        description="Required, repeating",
    )

    RXR: Optional[List[_RXR]] = Field(
        default=None,
        title="RXR",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
