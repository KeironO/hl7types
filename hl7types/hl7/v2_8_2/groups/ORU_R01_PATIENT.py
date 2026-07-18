"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: ORU_R01.PATIENT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.ARV import ARV
from ..segments.NK1 import NK1
from ..segments.NTE import NTE
from ..segments.PD1 import PD1
from ..segments.PID import PID
from ..segments.PRT import PRT

from .ORU_R01_PATIENT_OBSERVATION import ORU_R01_PATIENT_OBSERVATION
from .ORU_R01_VISIT import ORU_R01_VISIT

_ARV = ARV
_NK1 = NK1
_NTE = NTE
_ORU_R01_PATIENT_OBSERVATION = ORU_R01_PATIENT_OBSERVATION
_ORU_R01_VISIT = ORU_R01_VISIT
_PD1 = PD1
_PID = PID
_PRT = PRT


class ORU_R01_PATIENT(HL7Model):
    """HL7 v2 ORU_R01.PATIENT group.

    Attributes:
        PID (PID): Patient Identification, required
        PD1 (Optional[PD1]): Patient Additional Demographic, optional
        PRT (Optional[List[PRT]]): Participation Information, optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        NK1 (Optional[List[NK1]]): Next of Kin / Associated Parties, optional
        ARV (Optional[List[ARV]]): Access Restriction, optional
        PATIENT_OBSERVATION (Optional[List[ORU_R01_PATIENT_OBSERVATION]]): optional
        VISIT (Optional[ORU_R01_VISIT]): optional
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

    PATIENT_OBSERVATION: Optional[List[_ORU_R01_PATIENT_OBSERVATION]] = Field(
        default=None,
        title="PATIENT_OBSERVATION",
    )

    VISIT: Optional[_ORU_R01_VISIT] = Field(
        default=None,
        title="VISIT",
    )

    model_config = ConfigDict(populate_by_name=True)
