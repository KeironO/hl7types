"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: PEX_P07.ASSOCIATED_RX_ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.RXE import RXE
from ..segments.RXR import RXR

_RXE = RXE
_RXR = RXR


class PEX_P07_ASSOCIATED_RX_ORDER(HL7Model):
    """HL7 v2 PEX_P07.ASSOCIATED_RX_ORDER group.

    Attributes:
        RXE (RXE): Pharmacy/Treatment Encoded Order, required
        RXR (Optional[List[RXR]]): Pharmacy/Treatment Route, optional
    """

    RXE: _RXE = Field(
        title="RXE",
        description="Pharmacy/Treatment Encoded Order",
    )

    RXR: Optional[List[_RXR]] = Field(
        default=None,
        title="RXR",
        description="Pharmacy/Treatment Route",
    )

    model_config = {"populate_by_name": True}
