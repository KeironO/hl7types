"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
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
        RXE (RXE): RXE - pharmacy/treatment encoded order segment, required
        RXR (Optional[List[RXR]]): RXR - pharmacy/treatment route segment, optional
    """

    RXE: _RXE = Field(
        title="RXE",
        description="RXE - pharmacy/treatment encoded order segment",
    )

    RXR: Optional[List[_RXR]] = Field(
        default=None,
        title="RXR",
        description="RXR - pharmacy/treatment route segment",
    )

    model_config = {"populate_by_name": True}
