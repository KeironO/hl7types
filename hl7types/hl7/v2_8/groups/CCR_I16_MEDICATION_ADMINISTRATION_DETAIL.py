"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: CCR_I16.MEDICATION_ADMINISTRATION_DETAIL
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.RXA import RXA
from ..segments.RXR import RXR

from .CCR_I16_MEDICATION_ADMINISTRATION_OBSERVATION import CCR_I16_MEDICATION_ADMINISTRATION_OBSERVATION

_CCR_I16_MEDICATION_ADMINISTRATION_OBSERVATION = CCR_I16_MEDICATION_ADMINISTRATION_OBSERVATION
_RXA = RXA
_RXR = RXR


class CCR_I16_MEDICATION_ADMINISTRATION_DETAIL(HL7Model):
    """HL7 v2 CCR_I16.MEDICATION_ADMINISTRATION_DETAIL group.

    Attributes:
        RXA (List[RXA]): Pharmacy/Treatment Administration, required
        RXR (RXR): Pharmacy/Treatment Route, required
        MEDICATION_ADMINISTRATION_OBSERVATION (Optional[List[CCR_I16_MEDICATION_ADMINISTRATION_OBSERVATION]]): optional
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

    MEDICATION_ADMINISTRATION_OBSERVATION: Optional[List[_CCR_I16_MEDICATION_ADMINISTRATION_OBSERVATION]] = Field(
        default=None,
        title="MEDICATION_ADMINISTRATION_OBSERVATION",
    )

    model_config = ConfigDict(populate_by_name=True)
