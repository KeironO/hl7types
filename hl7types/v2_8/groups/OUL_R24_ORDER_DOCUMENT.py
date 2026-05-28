"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: OUL_R24.ORDER_DOCUMENT
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.OBX import OBX
from ..segments.PRT import PRT
from ..segments.TXA import TXA

_OBX = OBX
_PRT = PRT
_TXA = TXA


class OUL_R24_ORDER_DOCUMENT(BaseModel):
    """HL7 v2 OUL_R24.ORDER_DOCUMENT group.

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
