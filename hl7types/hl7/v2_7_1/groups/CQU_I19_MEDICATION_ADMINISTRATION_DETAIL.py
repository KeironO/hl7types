"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: CQU_I19.MEDICATION_ADMINISTRATION_DETAIL
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


class CQU_I19_MEDICATION_ADMINISTRATION_DETAIL(HL7Model):
    """HL7 v2 CQU_I19.MEDICATION_ADMINISTRATION_DETAIL group.

    Attributes:
        RXA (List[RXA]): Pharmacy/Treatment Administration, required
        RXR (RXR): Pharmacy/Treatment Route, required
        OBX (Optional[List[OBX]]): Observation/Result, optional
    """

    RXA: List[_RXA] = Field(
        min_length=1,
        title="RXA",
        description="Pharmacy/Treatment Administration",
    )

    RXR: _RXR = Field(
        title="RXR",
        description="Pharmacy/Treatment Route",
    )

    OBX: Optional[List[_OBX]] = Field(
        default=None,
        title="OBX",
        description="Observation/Result",
    )

    model_config = {"populate_by_name": True}
