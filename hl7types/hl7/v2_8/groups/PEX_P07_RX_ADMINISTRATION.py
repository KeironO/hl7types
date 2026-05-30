"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: PEX_P07.RX_ADMINISTRATION
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.PRT import PRT
from ..segments.RXA import RXA
from ..segments.RXR import RXR

_PRT = PRT
_RXA = RXA
_RXR = RXR


class PEX_P07_RX_ADMINISTRATION(HL7Model):
    """HL7 v2 PEX_P07.RX_ADMINISTRATION group.

    Attributes:
        RXA (RXA): required
        RXR (Optional[RXR]): optional
        PRT (Optional[List[PRT]]): optional
    """

    RXA: _RXA = Field(
        default=...,
        title="RXA",
        description="Required",
    )

    RXR: Optional[_RXR] = Field(
        default=None,
        title="RXR",
        description="Optional",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
