"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: CSU_C09.RX_ADMIN
Type: Group
"""

from __future__ import annotations

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

    PRT: list[_PRT] | None = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
