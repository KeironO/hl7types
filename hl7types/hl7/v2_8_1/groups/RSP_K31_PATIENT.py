"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: RSP_K31.PATIENT
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.AL1 import AL1
from ..segments.ARV import ARV
from ..segments.NTE import NTE
from ..segments.PID import PID
from .RSP_K31_ADDITIONAL_DEMOGRAPHICS import RSP_K31_ADDITIONAL_DEMOGRAPHICS
from .RSP_K31_PATIENT_VISIT import RSP_K31_PATIENT_VISIT

_AL1 = AL1
_ARV = ARV
_NTE = NTE
_PID = PID
_RSP_K31_ADDITIONAL_DEMOGRAPHICS = RSP_K31_ADDITIONAL_DEMOGRAPHICS
_RSP_K31_PATIENT_VISIT = RSP_K31_PATIENT_VISIT


class RSP_K31_PATIENT(BaseModel):
    """HL7 v2 RSP_K31.PATIENT group.

    Attributes:
        PID (PID): required
        ADDITIONAL_DEMOGRAPHICS (Optional[RSP_K31_ADDITIONAL_DEMOGRAPHICS]): optional
        NTE (Optional[List[NTE]]): optional
        ARV (Optional[List[ARV]]): optional
        AL1 (Optional[List[AL1]]): optional
        PATIENT_VISIT (Optional[RSP_K31_PATIENT_VISIT]): optional
    """

    PID: _PID = Field(
        default=...,
        title="PID",
        description="Required",
    )

    ADDITIONAL_DEMOGRAPHICS: _RSP_K31_ADDITIONAL_DEMOGRAPHICS | None = Field(
        default=None,
        title="ADDITIONAL_DEMOGRAPHICS",
        description="Optional",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    ARV: list[_ARV] | None = Field(
        default=None,
        title="ARV",
        description="Optional, repeating",
    )

    AL1: list[_AL1] | None = Field(
        default=None,
        title="AL1",
        description="Optional, repeating",
    )

    PATIENT_VISIT: _RSP_K31_PATIENT_VISIT | None = Field(
        default=None,
        title="PATIENT_VISIT",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
