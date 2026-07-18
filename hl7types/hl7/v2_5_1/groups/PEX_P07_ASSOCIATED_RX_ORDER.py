"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: PEX_P07.ASSOCIATED_RX_ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.RXE import RXE
from ..segments.RXR import RXR

from .PEX_P07_NK1_TIMING_QTY import PEX_P07_NK1_TIMING_QTY

_PEX_P07_NK1_TIMING_QTY = PEX_P07_NK1_TIMING_QTY
_RXE = RXE
_RXR = RXR


class PEX_P07_ASSOCIATED_RX_ORDER(HL7Model):
    """HL7 v2 PEX_P07.ASSOCIATED_RX_ORDER group.

    Attributes:
        RXE (RXE): Pharmacy/Treatment Encoded Order, required
        NK1_TIMING_QTY (List[PEX_P07_NK1_TIMING_QTY]): required
        RXR (Optional[List[RXR]]): Pharmacy/Treatment Route, optional
    """

    RXE: _RXE = Field(
        title="RXE",
        description="Pharmacy/Treatment Encoded Order",
    )

    NK1_TIMING_QTY: List[_PEX_P07_NK1_TIMING_QTY] = Field(
        min_length=1,
        title="NK1_TIMING_QTY",
    )

    RXR: Optional[List[_RXR]] = Field(
        default=None,
        title="RXR",
        description="Pharmacy/Treatment Route",
    )

    model_config = ConfigDict(populate_by_name=True)
