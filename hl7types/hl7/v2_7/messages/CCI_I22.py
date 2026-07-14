"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: CCI_I22
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.ERR import ERR
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.NK1 import NK1
from ..segments.PD1 import PD1
from ..segments.PID import PID
from ..segments.REL import REL
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.CCI_I22_APPOINTMENT_HISTORY import CCI_I22_APPOINTMENT_HISTORY
from ..groups.CCI_I22_CLINICAL_HISTORY import CCI_I22_CLINICAL_HISTORY
from ..groups.CCI_I22_GOAL import CCI_I22_GOAL
from ..groups.CCI_I22_INSURANCE import CCI_I22_INSURANCE
from ..groups.CCI_I22_MEDICATION_HISTORY import CCI_I22_MEDICATION_HISTORY
from ..groups.CCI_I22_PATHWAY import CCI_I22_PATHWAY
from ..groups.CCI_I22_PATIENT_VISITS import CCI_I22_PATIENT_VISITS
from ..groups.CCI_I22_PROBLEM import CCI_I22_PROBLEM

_CCI_I22_APPOINTMENT_HISTORY = CCI_I22_APPOINTMENT_HISTORY
_CCI_I22_CLINICAL_HISTORY = CCI_I22_CLINICAL_HISTORY
_CCI_I22_GOAL = CCI_I22_GOAL
_CCI_I22_INSURANCE = CCI_I22_INSURANCE
_CCI_I22_MEDICATION_HISTORY = CCI_I22_MEDICATION_HISTORY
_CCI_I22_PATHWAY = CCI_I22_PATHWAY
_CCI_I22_PATIENT_VISITS = CCI_I22_PATIENT_VISITS
_CCI_I22_PROBLEM = CCI_I22_PROBLEM
_ERR = ERR
_MSA = MSA
_MSH = MSH
_NK1 = NK1
_PD1 = PD1
_PID = PID
_REL = REL
_SFT = SFT
_UAC = UAC


class CCI_I22(HL7Model):
    """Collaborative Care Fetch / Collaborative Care Information (S11.7.2).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        MSA (MSA): Message Acknowledgment, required
        ERR (Optional[List[ERR]]): Error, optional
        PID (PID): Patient Identification, required
        PD1 (Optional[PD1]): Patient Additional Demographic, optional
        NK1 (Optional[List[NK1]]): Next of Kin / Associated Parties, optional
        INSURANCE (Optional[List[CCI_I22_INSURANCE]]): optional
        APPOINTMENT_HISTORY (Optional[List[CCI_I22_APPOINTMENT_HISTORY]]): optional
        CLINICAL_HISTORY (Optional[List[CCI_I22_CLINICAL_HISTORY]]): optional
        PATIENT_VISITS (List[CCI_I22_PATIENT_VISITS]): required
        MEDICATION_HISTORY (Optional[List[CCI_I22_MEDICATION_HISTORY]]): optional
        PROBLEM (Optional[List[CCI_I22_PROBLEM]]): optional
        GOAL (Optional[List[CCI_I22_GOAL]]): optional
        PATHWAY (Optional[List[CCI_I22_PATHWAY]]): optional
        REL (Optional[List[REL]]): Clinical Relationship Segment, optional
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

    MSA: _MSA = Field(
        title="MSA",
        description="Message Acknowledgment",
    )

    ERR: Optional[List[_ERR]] = Field(
        default=None,
        title="ERR",
        description="Error",
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

    INSURANCE: Optional[List[_CCI_I22_INSURANCE]] = Field(
        default=None,
        title="INSURANCE",
    )

    APPOINTMENT_HISTORY: Optional[List[_CCI_I22_APPOINTMENT_HISTORY]] = Field(
        default=None,
        title="APPOINTMENT_HISTORY",
    )

    CLINICAL_HISTORY: Optional[List[_CCI_I22_CLINICAL_HISTORY]] = Field(
        default=None,
        title="CLINICAL_HISTORY",
    )

    PATIENT_VISITS: List[_CCI_I22_PATIENT_VISITS] = Field(
        min_length=1,
        title="PATIENT_VISITS",
    )

    MEDICATION_HISTORY: Optional[List[_CCI_I22_MEDICATION_HISTORY]] = Field(
        default=None,
        title="MEDICATION_HISTORY",
    )

    PROBLEM: Optional[List[_CCI_I22_PROBLEM]] = Field(
        default=None,
        title="PROBLEM",
    )

    GOAL: Optional[List[_CCI_I22_GOAL]] = Field(
        default=None,
        title="GOAL",
    )

    PATHWAY: Optional[List[_CCI_I22_PATHWAY]] = Field(
        default=None,
        title="PATHWAY",
    )

    REL: Optional[List[_REL]] = Field(
        default=None,
        title="REL",
        description="Clinical Relationship Segment",
    )

    model_config = {"populate_by_name": True}
