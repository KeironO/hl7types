"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: ORX_O58.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.CTI import CTI
from ..segments.ORC import ORC
from ..segments.PRT import PRT
from ..segments.TXA import TXA

_CTI = CTI
_ORC = ORC
_PRT = PRT
_TXA = TXA


class ORX_O58_ORDER(HL7Model):
    """HL7 v2 ORX_O58.ORDER group.

    Attributes:
        ORC (ORC): required
        PRT (Optional[List[PRT]]): optional
        TXA (TXA): required
        CTI (Optional[List[CTI]]): optional
    """

    ORC: _ORC = Field(
        title="ORC",
        description="Required",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    TXA: _TXA = Field(
        title="TXA",
        description="Required",
    )

    CTI: Optional[List[_CTI]] = Field(
        default=None,
        title="CTI",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
