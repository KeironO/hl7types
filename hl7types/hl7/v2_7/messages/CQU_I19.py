"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: CQU_I19
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.ERR import ERR
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.NK1 import NK1
from ..segments.REL import REL
from ..segments.RF1 import RF1
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.CQU_I19_APPOINTMENT_HISTORY import CQU_I19_APPOINTMENT_HISTORY
from ..groups.CQU_I19_CLINICAL_HISTORY import CQU_I19_CLINICAL_HISTORY
from ..groups.CQU_I19_GOAL import CQU_I19_GOAL
from ..groups.CQU_I19_INSURANCE import CQU_I19_INSURANCE
from ..groups.CQU_I19_MEDICATION_HISTORY import CQU_I19_MEDICATION_HISTORY
from ..groups.CQU_I19_PATHWAY import CQU_I19_PATHWAY
from ..groups.CQU_I19_PATIENT import CQU_I19_PATIENT
from ..groups.CQU_I19_PATIENT_VISITS import CQU_I19_PATIENT_VISITS
from ..groups.CQU_I19_PROBLEM import CQU_I19_PROBLEM
from ..groups.CQU_I19_PROVIDER_CONTACT import CQU_I19_PROVIDER_CONTACT

_CQU_I19_APPOINTMENT_HISTORY = CQU_I19_APPOINTMENT_HISTORY
_CQU_I19_CLINICAL_HISTORY = CQU_I19_CLINICAL_HISTORY
_CQU_I19_GOAL = CQU_I19_GOAL
_CQU_I19_INSURANCE = CQU_I19_INSURANCE
_CQU_I19_MEDICATION_HISTORY = CQU_I19_MEDICATION_HISTORY
_CQU_I19_PATHWAY = CQU_I19_PATHWAY
_CQU_I19_PATIENT = CQU_I19_PATIENT
_CQU_I19_PATIENT_VISITS = CQU_I19_PATIENT_VISITS
_CQU_I19_PROBLEM = CQU_I19_PROBLEM
_CQU_I19_PROVIDER_CONTACT = CQU_I19_PROVIDER_CONTACT
_ERR = ERR
_MSA = MSA
_MSH = MSH
_NK1 = NK1
_REL = REL
_RF1 = RF1
_SFT = SFT
_UAC = UAC


class CQU_I19(HL7Model):
    """Collaborative Care Query/Collaborative Care Query Update (S11.7.1).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        MSA (MSA): Message Acknowledgment, required
        ERR (Optional[List[ERR]]): Error, optional
        RF1 (RF1): Referral Information, required
        PROVIDER_CONTACT (Optional[List[CQU_I19_PROVIDER_CONTACT]]): optional
        PATIENT (Optional[List[CQU_I19_PATIENT]]): optional
        NK1 (Optional[List[NK1]]): Next of Kin / Associated Parties, optional
        INSURANCE (Optional[List[CQU_I19_INSURANCE]]): optional
        APPOINTMENT_HISTORY (Optional[List[CQU_I19_APPOINTMENT_HISTORY]]): optional
        CLINICAL_HISTORY (Optional[List[CQU_I19_CLINICAL_HISTORY]]): optional
        PATIENT_VISITS (List[CQU_I19_PATIENT_VISITS]): required
        MEDICATION_HISTORY (Optional[List[CQU_I19_MEDICATION_HISTORY]]): optional
        PROBLEM (Optional[List[CQU_I19_PROBLEM]]): optional
        GOAL (Optional[List[CQU_I19_GOAL]]): optional
        PATHWAY (Optional[List[CQU_I19_PATHWAY]]): optional
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

    RF1: _RF1 = Field(
        title="RF1",
        description="Referral Information",
    )

    PROVIDER_CONTACT: Optional[List[_CQU_I19_PROVIDER_CONTACT]] = Field(
        default=None,
        title="PROVIDER_CONTACT",
    )

    PATIENT: Optional[List[_CQU_I19_PATIENT]] = Field(
        default=None,
        title="PATIENT",
    )

    NK1: Optional[List[_NK1]] = Field(
        default=None,
        title="NK1",
        description="Next of Kin / Associated Parties",
    )

    INSURANCE: Optional[List[_CQU_I19_INSURANCE]] = Field(
        default=None,
        title="INSURANCE",
    )

    APPOINTMENT_HISTORY: Optional[List[_CQU_I19_APPOINTMENT_HISTORY]] = Field(
        default=None,
        title="APPOINTMENT_HISTORY",
    )

    CLINICAL_HISTORY: Optional[List[_CQU_I19_CLINICAL_HISTORY]] = Field(
        default=None,
        title="CLINICAL_HISTORY",
    )

    PATIENT_VISITS: List[_CQU_I19_PATIENT_VISITS] = Field(
        min_length=1,
        title="PATIENT_VISITS",
    )

    MEDICATION_HISTORY: Optional[List[_CQU_I19_MEDICATION_HISTORY]] = Field(
        default=None,
        title="MEDICATION_HISTORY",
    )

    PROBLEM: Optional[List[_CQU_I19_PROBLEM]] = Field(
        default=None,
        title="PROBLEM",
    )

    GOAL: Optional[List[_CQU_I19_GOAL]] = Field(
        default=None,
        title="GOAL",
    )

    PATHWAY: Optional[List[_CQU_I19_PATHWAY]] = Field(
        default=None,
        title="PATHWAY",
    )

    REL: Optional[List[_REL]] = Field(
        default=None,
        title="REL",
        description="Clinical Relationship Segment",
    )

    model_config = ConfigDict(populate_by_name=True)
