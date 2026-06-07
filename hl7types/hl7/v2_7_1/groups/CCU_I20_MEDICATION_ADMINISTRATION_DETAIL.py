"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: CCU_I20.MEDICATION_ADMINISTRATION_DETAIL
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.OBX import OBX
from ..segments.RXA import RXA
from ..segments.RXR import RXR

_OBX = OBX
_RXA = RXA
_RXR = RXR


class CCU_I20_MEDICATION_ADMINISTRATION_DETAIL(HL7Model):
    """HL7 v2 CCU_I20.MEDICATION_ADMINISTRATION_DETAIL group.

    Attributes:
        RXA (List[RXA]): required
        RXR (RXR): required
        OBX (Optional[List[OBX]]): optional
    """

    RXA: List[_RXA] = Field(
        min_length=1,
        title="RXA",
        description="Required, repeating",
    )

    RXR: _RXR = Field(
        title="RXR",
        description="Required",
    )

    OBX: Optional[List[_OBX]] = Field(
        default=None,
        title="OBX",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
