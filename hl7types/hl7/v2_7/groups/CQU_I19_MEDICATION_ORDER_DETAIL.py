"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: CQU_I19.MEDICATION_ORDER_DETAIL
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.OBX import OBX
from ..segments.RXC import RXC
from ..segments.RXO import RXO
from ..segments.RXR import RXR

_OBX = OBX
_RXC = RXC
_RXO = RXO
_RXR = RXR


class CQU_I19_MEDICATION_ORDER_DETAIL(BaseModel):
    """HL7 v2 CQU_I19.MEDICATION_ORDER_DETAIL group.

    Attributes:
        RXO (RXO): required
        RXR (List[RXR]): required
        RXC (Optional[List[RXC]]): optional
        OBX (Optional[List[OBX]]): optional
    """

    RXO: _RXO = Field(
        default=...,
        title="RXO",
        description="Required",
    )

    RXR: list[_RXR] = Field(
        default=...,
        title="RXR",
        description="Required, repeating",
    )

    RXC: list[_RXC] | None = Field(
        default=None,
        title="RXC",
        description="Optional, repeating",
    )

    OBX: list[_OBX] | None = Field(
        default=None,
        title="OBX",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
