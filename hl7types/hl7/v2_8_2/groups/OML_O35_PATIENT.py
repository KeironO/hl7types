"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: OML_O35.PATIENT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.AL1 import AL1
from ..segments.ARV import ARV
from ..segments.GT1 import GT1
from ..segments.NK1 import NK1
from ..segments.NTE import NTE
from ..segments.PD1 import PD1
from ..segments.PID import PID
from ..segments.PRT import PRT

from .OML_O35_INSURANCE import OML_O35_INSURANCE
from .OML_O35_PATIENT_VISIT import OML_O35_PATIENT_VISIT

_AL1 = AL1
_ARV = ARV
_GT1 = GT1
_NK1 = NK1
_NTE = NTE
_OML_O35_INSURANCE = OML_O35_INSURANCE
_OML_O35_PATIENT_VISIT = OML_O35_PATIENT_VISIT
_PD1 = PD1
_PID = PID
_PRT = PRT


class OML_O35_PATIENT(HL7Model):
    """HL7 v2 OML_O35.PATIENT group.

    Attributes:
        PID (PID): Patient Identification, required
        PD1 (Optional[PD1]): Patient Additional Demographic, optional
        PRT (Optional[List[PRT]]): Participation Information, optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        NK1 (Optional[List[NK1]]): Next of Kin / Associated Parties, optional
        ARV (Optional[List[ARV]]): Access Restriction, optional
        PATIENT_VISIT (Optional[OML_O35_PATIENT_VISIT]): optional
        INSURANCE (Optional[List[OML_O35_INSURANCE]]): optional
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

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    NK1: Optional[List[_NK1]] = Field(
        default=None,
        title="NK1",
        description="Next of Kin / Associated Parties",
    )

    ARV: Optional[List[_ARV]] = Field(
        default=None,
        title="ARV",
        description="Access Restriction",
    )

    PATIENT_VISIT: Optional[_OML_O35_PATIENT_VISIT] = Field(
        default=None,
        title="PATIENT_VISIT",
    )

    INSURANCE: Optional[List[_OML_O35_INSURANCE]] = Field(
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
