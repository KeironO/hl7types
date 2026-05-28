"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: CCI_I22.MEDICATION_ADMINISTRATION_DETAIL
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.OBX import OBX
from ..segments.RXA import RXA
from ..segments.RXR import RXR

_OBX = OBX
_RXA = RXA
_RXR = RXR


class CCI_I22_MEDICATION_ADMINISTRATION_DETAIL(BaseModel):
    """HL7 v2 CCI_I22.MEDICATION_ADMINISTRATION_DETAIL group.

    Attributes:
        RXA (List[RXA]): required
        RXR (RXR): required
        OBX (Optional[List[OBX]]): optional
    """

    RXA: list[_RXA] = Field(
        default=...,
        title="RXA",
        description="Required, repeating",
    )

    RXR: _RXR = Field(
        default=...,
        title="RXR",
        description="Required",
    )

    OBX: list[_OBX] | None = Field(
        default=None,
        title="OBX",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
