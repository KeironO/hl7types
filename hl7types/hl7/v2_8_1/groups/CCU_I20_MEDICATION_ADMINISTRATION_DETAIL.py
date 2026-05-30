"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: CCU_I20.MEDICATION_ADMINISTRATION_DETAIL
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.RXA import RXA
from ..segments.RXR import RXR

from .CCU_I20_MEDICATION_ADMINISTRATION_OBSERVATION import CCU_I20_MEDICATION_ADMINISTRATION_OBSERVATION

_CCU_I20_MEDICATION_ADMINISTRATION_OBSERVATION = CCU_I20_MEDICATION_ADMINISTRATION_OBSERVATION
_RXA = RXA
_RXR = RXR


class CCU_I20_MEDICATION_ADMINISTRATION_DETAIL(HL7Model):
    """HL7 v2 CCU_I20.MEDICATION_ADMINISTRATION_DETAIL group.

    Attributes:
        RXA (List[RXA]): required
        RXR (RXR): required
        MEDICATION_ADMINISTRATION_OBSERVATION (Optional[List[CCU_I20_MEDICATION_ADMINISTRATION_OBSERVATION]]): optional
    """

    RXA: List[_RXA] = Field(
        default=...,
        title="RXA",
        description="Required, repeating",
    )

    RXR: _RXR = Field(
        default=...,
        title="RXR",
        description="Required",
    )

    MEDICATION_ADMINISTRATION_OBSERVATION: Optional[List[_CCU_I20_MEDICATION_ADMINISTRATION_OBSERVATION]] = Field(
        default=None,
        title="MEDICATION_ADMINISTRATION_OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
