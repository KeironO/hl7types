"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: RAS_O17.PATIENT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.AL1 import AL1
from ..segments.ARV import ARV
from ..segments.NTE import NTE
from ..segments.PID import PID

from .RAS_O17_ADDITIONAL_DEMOGRAPHICS import RAS_O17_ADDITIONAL_DEMOGRAPHICS
from .RAS_O17_PATIENT_VISIT import RAS_O17_PATIENT_VISIT

_AL1 = AL1
_ARV = ARV
_NTE = NTE
_PID = PID
_RAS_O17_ADDITIONAL_DEMOGRAPHICS = RAS_O17_ADDITIONAL_DEMOGRAPHICS
_RAS_O17_PATIENT_VISIT = RAS_O17_PATIENT_VISIT


class RAS_O17_PATIENT(HL7Model):
    """HL7 v2 RAS_O17.PATIENT group.

    Attributes:
        PID (PID): Patient Identification, required
        ADDITIONAL_DEMOGRAPHICS (Optional[RAS_O17_ADDITIONAL_DEMOGRAPHICS]): optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        ARV (Optional[List[ARV]]): Access Restriction, optional
        AL1 (Optional[List[AL1]]): Patient Allergy Information, optional
        PATIENT_VISIT (Optional[RAS_O17_PATIENT_VISIT]): optional
    """

    PID: _PID = Field(
        title="PID",
        description="Patient Identification",
    )

    ADDITIONAL_DEMOGRAPHICS: Optional[_RAS_O17_ADDITIONAL_DEMOGRAPHICS] = Field(
        default=None,
        title="ADDITIONAL_DEMOGRAPHICS",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    ARV: Optional[List[_ARV]] = Field(
        default=None,
        title="ARV",
        description="Access Restriction",
    )

    AL1: Optional[List[_AL1]] = Field(
        default=None,
        title="AL1",
        description="Patient Allergy Information",
    )

    PATIENT_VISIT: Optional[_RAS_O17_PATIENT_VISIT] = Field(
        default=None,
        title="PATIENT_VISIT",
    )

    model_config = ConfigDict(populate_by_name=True)
