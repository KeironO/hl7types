"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: RDE_O11.PATIENT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.AL1 import AL1
from ..segments.ARV import ARV
from ..segments.GT1 import GT1
from ..segments.NTE import NTE
from ..segments.PD1 import PD1
from ..segments.PID import PID
from ..segments.PRT import PRT

from .RDE_O11_INSURANCE import RDE_O11_INSURANCE
from .RDE_O11_PATIENT_VISIT import RDE_O11_PATIENT_VISIT

_AL1 = AL1
_ARV = ARV
_GT1 = GT1
_NTE = NTE
_PD1 = PD1
_PID = PID
_PRT = PRT
_RDE_O11_INSURANCE = RDE_O11_INSURANCE
_RDE_O11_PATIENT_VISIT = RDE_O11_PATIENT_VISIT


class RDE_O11_PATIENT(HL7Model):
    """HL7 v2 RDE_O11.PATIENT group.

    Attributes:
        PID (PID): required
        PD1 (Optional[PD1]): optional
        PRT (Optional[List[PRT]]): optional
        NTE (Optional[List[NTE]]): optional
        ARV (Optional[List[ARV]]): optional
        PATIENT_VISIT (Optional[RDE_O11_PATIENT_VISIT]): optional
        INSURANCE (Optional[List[RDE_O11_INSURANCE]]): optional
        GT1 (Optional[GT1]): optional
        AL1 (Optional[List[AL1]]): optional
    """

    PID: _PID = Field(
        default=...,
        title="PID",
        description="Required",
    )

    PD1: Optional[_PD1] = Field(
        default=None,
        title="PD1",
        description="Optional",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
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

    PATIENT_VISIT: Optional[_RDE_O11_PATIENT_VISIT] = Field(
        default=None,
        title="PATIENT_VISIT",
        description="Optional",
    )

    INSURANCE: Optional[List[_RDE_O11_INSURANCE]] = Field(
        default=None,
        title="INSURANCE",
        description="Optional, repeating",
    )

    GT1: Optional[_GT1] = Field(
        default=None,
        title="GT1",
        description="Optional",
    )

    AL1: Optional[List[_AL1]] = Field(
        default=None,
        title="AL1",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
