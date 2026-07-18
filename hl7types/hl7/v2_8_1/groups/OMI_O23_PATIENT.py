"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: OMI_O23.PATIENT
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
from ..segments.PD1 import PD1
from ..segments.PID import PID
from ..segments.PRT import PRT

from .OMI_O23_INSURANCE import OMI_O23_INSURANCE
from .OMI_O23_PATIENT_VISIT import OMI_O23_PATIENT_VISIT

_AL1 = AL1
_ARV = ARV
_GT1 = GT1
_NTE = NTE
_OMI_O23_INSURANCE = OMI_O23_INSURANCE
_OMI_O23_PATIENT_VISIT = OMI_O23_PATIENT_VISIT
_PD1 = PD1
_PID = PID
_PRT = PRT


class OMI_O23_PATIENT(HL7Model):
    """HL7 v2 OMI_O23.PATIENT group.

    Attributes:
        PID (PID): Patient Identification, required
        PD1 (Optional[PD1]): Patient Additional Demographic, optional
        PRT (Optional[List[PRT]]): Participation Information, optional
        ARV (Optional[List[ARV]]): Access Restriction, optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        PATIENT_VISIT (Optional[OMI_O23_PATIENT_VISIT]): optional
        INSURANCE (Optional[List[OMI_O23_INSURANCE]]): optional
        GT1 (Optional[GT1]): Guarantor, optional
        AL1 (Optional[List[AL1]]): Patient Allergy Information, optional
    """

    PID: _PID = Field(
        title="PID",
        description="Patient Identification",
    )

    PD1: Optional[_PD1] = Field(
        default=None,
        title="PD1",
        description="Patient Additional Demographic",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Participation Information",
    )

    ARV: Optional[List[_ARV]] = Field(
        default=None,
        title="ARV",
        description="Access Restriction",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    PATIENT_VISIT: Optional[_OMI_O23_PATIENT_VISIT] = Field(
        default=None,
        title="PATIENT_VISIT",
    )

    INSURANCE: Optional[List[_OMI_O23_INSURANCE]] = Field(
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
