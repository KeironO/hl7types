"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: CCM_I21.MEDICATION_ADMINISTRATION_DETAIL
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.RXA import RXA
from ..segments.RXR import RXR

from .CCM_I21_MEDICATION_ADMINISTRATION_OBSERVATION import CCM_I21_MEDICATION_ADMINISTRATION_OBSERVATION

_CCM_I21_MEDICATION_ADMINISTRATION_OBSERVATION = CCM_I21_MEDICATION_ADMINISTRATION_OBSERVATION
_RXA = RXA
_RXR = RXR


class CCM_I21_MEDICATION_ADMINISTRATION_DETAIL(BaseModel):
    """HL7 v2 CCM_I21.MEDICATION_ADMINISTRATION_DETAIL group.

    Attributes:
        RXA (List[RXA]): required
        RXR (RXR): required
        MEDICATION_ADMINISTRATION_OBSERVATION (Optional[List[CCM_I21_MEDICATION_ADMINISTRATION_OBSERVATION]]): optional
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

    MEDICATION_ADMINISTRATION_OBSERVATION: Optional[List[_CCM_I21_MEDICATION_ADMINISTRATION_OBSERVATION]] = Field(
        default=None,
        title="MEDICATION_ADMINISTRATION_OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
