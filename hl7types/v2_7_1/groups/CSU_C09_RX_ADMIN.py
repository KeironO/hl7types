"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: CSU_C09.RX_ADMIN
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.PRT import PRT
from ..segments.RXA import RXA
from ..segments.RXR import RXR

_PRT = PRT
_RXA = RXA
_RXR = RXR


class CSU_C09_RX_ADMIN(BaseModel):
    """HL7 v2 CSU_C09.RX_ADMIN group.

    Attributes:
        RXA (RXA): required
        RXR (RXR): required
        PRT (Optional[List[PRT]]): optional
    """

    RXA: _RXA = Field(
        default=...,
        title="RXA",
        description="Required",
    )

    RXR: _RXR = Field(
        default=...,
        title="RXR",
        description="Required",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
