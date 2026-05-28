"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: CQU_I19.MEDICATION_ADMINISTRATION_DETAIL
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.RXA import RXA
from ..segments.RXR import RXR
from .CQU_I19_MEDICATION_ADMINISTRATION_OBSERVATION import (
    CQU_I19_MEDICATION_ADMINISTRATION_OBSERVATION,
)

_CQU_I19_MEDICATION_ADMINISTRATION_OBSERVATION = CQU_I19_MEDICATION_ADMINISTRATION_OBSERVATION
_RXA = RXA
_RXR = RXR


class CQU_I19_MEDICATION_ADMINISTRATION_DETAIL(BaseModel):
    """HL7 v2 CQU_I19.MEDICATION_ADMINISTRATION_DETAIL group.

    Attributes:
        RXA (List[RXA]): required
        RXR (RXR): required
        MEDICATION_ADMINISTRATION_OBSERVATION (Optional[List[CQU_I19_MEDICATION_ADMINISTRATION_OBSERVATION]]): optional
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

    MEDICATION_ADMINISTRATION_OBSERVATION: (
        list[_CQU_I19_MEDICATION_ADMINISTRATION_OBSERVATION] | None
    ) = Field(
        default=None,
        title="MEDICATION_ADMINISTRATION_OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
