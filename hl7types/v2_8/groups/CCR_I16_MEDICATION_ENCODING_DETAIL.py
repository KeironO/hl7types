"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: CCR_I16.MEDICATION_ENCODING_DETAIL
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.RXC import RXC
from ..segments.RXE import RXE
from ..segments.RXR import RXR

from .CCR_I16_MEDICATION_ENCODING_OBSERVATION import CCR_I16_MEDICATION_ENCODING_OBSERVATION

_CCR_I16_MEDICATION_ENCODING_OBSERVATION = CCR_I16_MEDICATION_ENCODING_OBSERVATION
_RXC = RXC
_RXE = RXE
_RXR = RXR


class CCR_I16_MEDICATION_ENCODING_DETAIL(BaseModel):
    """HL7 v2 CCR_I16.MEDICATION_ENCODING_DETAIL group.

    Attributes:
        RXE (RXE): required
        RXR (List[RXR]): required
        RXC (Optional[List[RXC]]): optional
        MEDICATION_ENCODING_OBSERVATION (Optional[List[CCR_I16_MEDICATION_ENCODING_OBSERVATION]]): optional
    """

    RXE: _RXE = Field(
        default=...,
        title="RXE",
        description="Required",
    )

    RXR: List[_RXR] = Field(
        default=...,
        title="RXR",
        description="Required, repeating",
    )

    RXC: Optional[List[_RXC]] = Field(
        default=None,
        title="RXC",
        description="Optional, repeating",
    )

    MEDICATION_ENCODING_OBSERVATION: Optional[List[_CCR_I16_MEDICATION_ENCODING_OBSERVATION]] = Field(
        default=None,
        title="MEDICATION_ENCODING_OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
