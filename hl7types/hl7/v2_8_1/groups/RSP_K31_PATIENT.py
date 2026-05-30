"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: RSP_K31.PATIENT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

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


class RSP_K31_PATIENT(HL7Model):
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

    ADDITIONAL_DEMOGRAPHICS: Optional[_RSP_K31_ADDITIONAL_DEMOGRAPHICS] = Field(
        default=None,
        title="ADDITIONAL_DEMOGRAPHICS",
        description="Optional",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    ARV: Optional[List[_ARV]] = Field(
        default=None,
        title="ARV",
        description="Optional, repeating",
    )

    AL1: Optional[List[_AL1]] = Field(
        default=None,
        title="AL1",
        description="Optional, repeating",
    )

    PATIENT_VISIT: Optional[_RSP_K31_PATIENT_VISIT] = Field(
        default=None,
        title="PATIENT_VISIT",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
