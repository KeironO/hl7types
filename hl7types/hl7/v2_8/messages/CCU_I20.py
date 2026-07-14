"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: CCU_I20
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH
from ..segments.NK1 import NK1
from ..segments.REL import REL
from ..segments.RF1 import RF1
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.CCU_I20_APPOINTMENT_HISTORY import CCU_I20_APPOINTMENT_HISTORY
from ..groups.CCU_I20_CLINICAL_HISTORY import CCU_I20_CLINICAL_HISTORY
from ..groups.CCU_I20_GOAL import CCU_I20_GOAL
from ..groups.CCU_I20_INSURANCE import CCU_I20_INSURANCE
from ..groups.CCU_I20_MEDICATION_HISTORY import CCU_I20_MEDICATION_HISTORY
from ..groups.CCU_I20_PATHWAY import CCU_I20_PATHWAY
from ..groups.CCU_I20_PATIENT import CCU_I20_PATIENT
from ..groups.CCU_I20_PATIENT_VISITS import CCU_I20_PATIENT_VISITS
from ..groups.CCU_I20_PROBLEM import CCU_I20_PROBLEM
from ..groups.CCU_I20_PROVIDER_CONTACT import CCU_I20_PROVIDER_CONTACT

_CCU_I20_APPOINTMENT_HISTORY = CCU_I20_APPOINTMENT_HISTORY
_CCU_I20_CLINICAL_HISTORY = CCU_I20_CLINICAL_HISTORY
_CCU_I20_GOAL = CCU_I20_GOAL
_CCU_I20_INSURANCE = CCU_I20_INSURANCE
_CCU_I20_MEDICATION_HISTORY = CCU_I20_MEDICATION_HISTORY
_CCU_I20_PATHWAY = CCU_I20_PATHWAY
_CCU_I20_PATIENT = CCU_I20_PATIENT
_CCU_I20_PATIENT_VISITS = CCU_I20_PATIENT_VISITS
_CCU_I20_PROBLEM = CCU_I20_PROBLEM
_CCU_I20_PROVIDER_CONTACT = CCU_I20_PROVIDER_CONTACT
_MSH = MSH
_NK1 = NK1
_REL = REL
_RF1 = RF1
_SFT = SFT
_UAC = UAC


class CCU_I20(HL7Model):
    """Asynchronous Collaborative Care Update (S11.6.6).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        RF1 (RF1): Referral Information, required
        PROVIDER_CONTACT (Optional[List[CCU_I20_PROVIDER_CONTACT]]): optional
        PATIENT (Optional[List[CCU_I20_PATIENT]]): optional
        NK1 (Optional[List[NK1]]): Next of Kin / Associated Parties, optional
        INSURANCE (Optional[List[CCU_I20_INSURANCE]]): optional
        APPOINTMENT_HISTORY (Optional[List[CCU_I20_APPOINTMENT_HISTORY]]): optional
        CLINICAL_HISTORY (Optional[List[CCU_I20_CLINICAL_HISTORY]]): optional
        PATIENT_VISITS (List[CCU_I20_PATIENT_VISITS]): required
        MEDICATION_HISTORY (Optional[List[CCU_I20_MEDICATION_HISTORY]]): optional
        PROBLEM (Optional[List[CCU_I20_PROBLEM]]): optional
        GOAL (Optional[List[CCU_I20_GOAL]]): optional
        PATHWAY (Optional[List[CCU_I20_PATHWAY]]): optional
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

    RF1: _RF1 = Field(
        title="RF1",
        description="Referral Information",
    )

    PROVIDER_CONTACT: Optional[List[_CCU_I20_PROVIDER_CONTACT]] = Field(
        default=None,
        title="PROVIDER_CONTACT",
    )

    PATIENT: Optional[List[_CCU_I20_PATIENT]] = Field(
        default=None,
        title="PATIENT",
    )

    NK1: Optional[List[_NK1]] = Field(
        default=None,
        title="NK1",
        description="Next of Kin / Associated Parties",
    )

    INSURANCE: Optional[List[_CCU_I20_INSURANCE]] = Field(
        default=None,
        title="INSURANCE",
    )

    APPOINTMENT_HISTORY: Optional[List[_CCU_I20_APPOINTMENT_HISTORY]] = Field(
        default=None,
        title="APPOINTMENT_HISTORY",
    )

    CLINICAL_HISTORY: Optional[List[_CCU_I20_CLINICAL_HISTORY]] = Field(
        default=None,
        title="CLINICAL_HISTORY",
    )

    PATIENT_VISITS: List[_CCU_I20_PATIENT_VISITS] = Field(
        min_length=1,
        title="PATIENT_VISITS",
    )

    MEDICATION_HISTORY: Optional[List[_CCU_I20_MEDICATION_HISTORY]] = Field(
        default=None,
        title="MEDICATION_HISTORY",
    )

    PROBLEM: Optional[List[_CCU_I20_PROBLEM]] = Field(
        default=None,
        title="PROBLEM",
    )

    GOAL: Optional[List[_CCU_I20_GOAL]] = Field(
        default=None,
        title="GOAL",
    )

    PATHWAY: Optional[List[_CCU_I20_PATHWAY]] = Field(
        default=None,
        title="PATHWAY",
    )

    REL: Optional[List[_REL]] = Field(
        default=None,
        title="REL",
        description="Clinical Relationship Segment",
    )

    model_config = {"populate_by_name": True}
