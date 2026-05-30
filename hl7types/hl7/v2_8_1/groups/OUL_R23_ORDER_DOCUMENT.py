"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: OUL_R23.ORDER_DOCUMENT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.OBX import OBX
from ..segments.PRT import PRT
from ..segments.TXA import TXA

_OBX = OBX
_PRT = PRT
_TXA = TXA


class OUL_R23_ORDER_DOCUMENT(HL7Model):
    """HL7 v2 OUL_R23.ORDER_DOCUMENT group.

    Attributes:
        OBX (OBX): required
        PRT (Optional[List[PRT]]): optional
        TXA (TXA): required
    """

    OBX: _OBX = Field(
        default=...,
        title="OBX",
        description="Required",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    TXA: _TXA = Field(
        default=...,
        title="TXA",
        description="Required",
    )

    model_config = {"populate_by_name": True}
