"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: OMP_O09.PATIENT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.AL1 import AL1
from ..segments.ARV import ARV
from ..segments.GT1 import GT1
from ..segments.NTE import NTE
from ..segments.PID import PID

from .OMP_O09_ADDITIONAL_DEMOGRAPHICS import OMP_O09_ADDITIONAL_DEMOGRAPHICS
from .OMP_O09_INSURANCE import OMP_O09_INSURANCE
from .OMP_O09_PATIENT_VISIT import OMP_O09_PATIENT_VISIT

_AL1 = AL1
_ARV = ARV
_GT1 = GT1
_NTE = NTE
_OMP_O09_ADDITIONAL_DEMOGRAPHICS = OMP_O09_ADDITIONAL_DEMOGRAPHICS
_OMP_O09_INSURANCE = OMP_O09_INSURANCE
_OMP_O09_PATIENT_VISIT = OMP_O09_PATIENT_VISIT
_PID = PID


class OMP_O09_PATIENT(HL7Model):
    """HL7 v2 OMP_O09.PATIENT group.

    Attributes:
        PID (PID): Patient Identification, required
        ADDITIONAL_DEMOGRAPHICS (Optional[OMP_O09_ADDITIONAL_DEMOGRAPHICS]): optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        ARV (Optional[List[ARV]]): Access Restriction, optional
        PATIENT_VISIT (Optional[OMP_O09_PATIENT_VISIT]): optional
        INSURANCE (Optional[List[OMP_O09_INSURANCE]]): optional
        GT1 (Optional[GT1]): Guarantor, optional
        AL1 (Optional[List[AL1]]): Patient Allergy Information, optional
    """

    PID: _PID = Field(
        title="PID",
        description="Patient Identification",
    )

    ADDITIONAL_DEMOGRAPHICS: Optional[_OMP_O09_ADDITIONAL_DEMOGRAPHICS] = Field(
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

    PATIENT_VISIT: Optional[_OMP_O09_PATIENT_VISIT] = Field(
        default=None,
        title="PATIENT_VISIT",
    )

    INSURANCE: Optional[List[_OMP_O09_INSURANCE]] = Field(
        default=None,
        title="INSURANCE",
    )

    GT1: Optional[_GT1] = Field(
        default=None,
        title="GT1",
        description="Guarantor",
    )

    AL1: Optional[List[_AL1]] = Field(
        default=None,
        title="AL1",
        description="Patient Allergy Information",
    )

    model_config = ConfigDict(populate_by_name=True)
