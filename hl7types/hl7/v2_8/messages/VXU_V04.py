"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: VXU_V04
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.ARV import ARV
from ..segments.GT1 import GT1
from ..segments.MSH import MSH
from ..segments.NK1 import NK1
from ..segments.PD1 import PD1
from ..segments.PID import PID
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.VXU_V04_INSURANCE import VXU_V04_INSURANCE
from ..groups.VXU_V04_ORDER import VXU_V04_ORDER
from ..groups.VXU_V04_PATIENT_VISIT import VXU_V04_PATIENT_VISIT
from ..groups.VXU_V04_PERSON_OBSERVATION import VXU_V04_PERSON_OBSERVATION

_ARV = ARV
_GT1 = GT1
_MSH = MSH
_NK1 = NK1
_PD1 = PD1
_PID = PID
_SFT = SFT
_UAC = UAC
_VXU_V04_INSURANCE = VXU_V04_INSURANCE
_VXU_V04_ORDER = VXU_V04_ORDER
_VXU_V04_PATIENT_VISIT = VXU_V04_PATIENT_VISIT
_VXU_V04_PERSON_OBSERVATION = VXU_V04_PERSON_OBSERVATION


class VXU_V04(HL7Model):
    """VXU - Unsolicited vaccination record update (S4.A.6).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        PID (PID): Patient Identification, required
        PD1 (Optional[PD1]): Patient Additional Demographic, optional
        NK1 (Optional[List[NK1]]): Next of Kin / Associated Parties, optional
        ARV (Optional[List[ARV]]): Access Restriction, optional
        PATIENT_VISIT (Optional[VXU_V04_PATIENT_VISIT]): optional
        GT1 (Optional[List[GT1]]): Guarantor, optional
        INSURANCE (Optional[List[VXU_V04_INSURANCE]]): optional
        PERSON_OBSERVATION (Optional[List[VXU_V04_PERSON_OBSERVATION]]): optional
        ORDER (Optional[List[VXU_V04_ORDER]]): optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message Header",
    )

    SFT: Optional[List[_SFT]] = Field(
        default=None,
        title="SFT",
        description="Software Segment",
    )

    UAC: Optional[_UAC] = Field(
        default=None,
        title="UAC",
        description="User Authentication Credential Segment",
    )

    PID: _PID = Field(
        title="PID",
        description="Patient Identification",
    )

    PD1: Optional[_PD1] = Field(
        default=None,
        title="PD1",
        description="Patient Additional Demographic",
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

    PATIENT_VISIT: Optional[_VXU_V04_PATIENT_VISIT] = Field(
        default=None,
        title="PATIENT_VISIT",
    )

    GT1: Optional[List[_GT1]] = Field(
        default=None,
        title="GT1",
        description="Guarantor",
    )

    INSURANCE: Optional[List[_VXU_V04_INSURANCE]] = Field(
        default=None,
        title="INSURANCE",
    )

    PERSON_OBSERVATION: Optional[List[_VXU_V04_PERSON_OBSERVATION]] = Field(
        default=None,
        title="PERSON_OBSERVATION",
    )

    ORDER: Optional[List[_VXU_V04_ORDER]] = Field(
        default=None,
        title="ORDER",
    )

    model_config = ConfigDict(populate_by_name=True)
