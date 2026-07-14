"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: CCR_I16
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

from ..groups.CCR_I16_APPOINTMENT_HISTORY import CCR_I16_APPOINTMENT_HISTORY
from ..groups.CCR_I16_CLINICAL_HISTORY import CCR_I16_CLINICAL_HISTORY
from ..groups.CCR_I16_CLINICAL_ORDER import CCR_I16_CLINICAL_ORDER
from ..groups.CCR_I16_GOAL import CCR_I16_GOAL
from ..groups.CCR_I16_INSURANCE import CCR_I16_INSURANCE
from ..groups.CCR_I16_MEDICATION_HISTORY import CCR_I16_MEDICATION_HISTORY
from ..groups.CCR_I16_PATHWAY import CCR_I16_PATHWAY
from ..groups.CCR_I16_PATIENT import CCR_I16_PATIENT
from ..groups.CCR_I16_PATIENT_VISITS import CCR_I16_PATIENT_VISITS
from ..groups.CCR_I16_PROBLEM import CCR_I16_PROBLEM
from ..groups.CCR_I16_PROVIDER_CONTACT import CCR_I16_PROVIDER_CONTACT

_CCR_I16_APPOINTMENT_HISTORY = CCR_I16_APPOINTMENT_HISTORY
_CCR_I16_CLINICAL_HISTORY = CCR_I16_CLINICAL_HISTORY
_CCR_I16_CLINICAL_ORDER = CCR_I16_CLINICAL_ORDER
_CCR_I16_GOAL = CCR_I16_GOAL
_CCR_I16_INSURANCE = CCR_I16_INSURANCE
_CCR_I16_MEDICATION_HISTORY = CCR_I16_MEDICATION_HISTORY
_CCR_I16_PATHWAY = CCR_I16_PATHWAY
_CCR_I16_PATIENT = CCR_I16_PATIENT
_CCR_I16_PATIENT_VISITS = CCR_I16_PATIENT_VISITS
_CCR_I16_PROBLEM = CCR_I16_PROBLEM
_CCR_I16_PROVIDER_CONTACT = CCR_I16_PROVIDER_CONTACT
_MSH = MSH
_NK1 = NK1
_REL = REL
_RF1 = RF1
_SFT = SFT
_UAC = UAC


class CCR_I16(HL7Model):
    """Collaborative Care Referral (S11.5.2).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        RF1 (List[RF1]): Referral Information, required
        PROVIDER_CONTACT (List[CCR_I16_PROVIDER_CONTACT]): required
        CLINICAL_ORDER (Optional[List[CCR_I16_CLINICAL_ORDER]]): optional
        PATIENT (List[CCR_I16_PATIENT]): required
        NK1 (Optional[List[NK1]]): Next of Kin / Associated Parties, optional
        INSURANCE (Optional[List[CCR_I16_INSURANCE]]): optional
        APPOINTMENT_HISTORY (Optional[List[CCR_I16_APPOINTMENT_HISTORY]]): optional
        CLINICAL_HISTORY (Optional[List[CCR_I16_CLINICAL_HISTORY]]): optional
        PATIENT_VISITS (List[CCR_I16_PATIENT_VISITS]): required
        MEDICATION_HISTORY (Optional[List[CCR_I16_MEDICATION_HISTORY]]): optional
        PROBLEM (Optional[List[CCR_I16_PROBLEM]]): optional
        GOAL (Optional[List[CCR_I16_GOAL]]): optional
        PATHWAY (Optional[List[CCR_I16_PATHWAY]]): optional
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

    RF1: List[_RF1] = Field(
        min_length=1,
        title="RF1",
        description="Referral Information",
    )

    PROVIDER_CONTACT: List[_CCR_I16_PROVIDER_CONTACT] = Field(
        min_length=1,
        title="PROVIDER_CONTACT",
    )

    CLINICAL_ORDER: Optional[List[_CCR_I16_CLINICAL_ORDER]] = Field(
        default=None,
        title="CLINICAL_ORDER",
    )

    PATIENT: List[_CCR_I16_PATIENT] = Field(
        min_length=1,
        title="PATIENT",
    )

    NK1: Optional[List[_NK1]] = Field(
        default=None,
        title="NK1",
        description="Next of Kin / Associated Parties",
    )

    INSURANCE: Optional[List[_CCR_I16_INSURANCE]] = Field(
        default=None,
        title="INSURANCE",
    )

    APPOINTMENT_HISTORY: Optional[List[_CCR_I16_APPOINTMENT_HISTORY]] = Field(
        default=None,
        title="APPOINTMENT_HISTORY",
    )

    CLINICAL_HISTORY: Optional[List[_CCR_I16_CLINICAL_HISTORY]] = Field(
        default=None,
        title="CLINICAL_HISTORY",
    )

    PATIENT_VISITS: List[_CCR_I16_PATIENT_VISITS] = Field(
        min_length=1,
        title="PATIENT_VISITS",
    )

    MEDICATION_HISTORY: Optional[List[_CCR_I16_MEDICATION_HISTORY]] = Field(
        default=None,
        title="MEDICATION_HISTORY",
    )

    PROBLEM: Optional[List[_CCR_I16_PROBLEM]] = Field(
        default=None,
        title="PROBLEM",
    )

    GOAL: Optional[List[_CCR_I16_GOAL]] = Field(
        default=None,
        title="GOAL",
    )

    PATHWAY: Optional[List[_CCR_I16_PATHWAY]] = Field(
        default=None,
        title="PATHWAY",
    )

    REL: Optional[List[_REL]] = Field(
        default=None,
        title="REL",
        description="Clinical Relationship Segment",
    )

    model_config = {"populate_by_name": True}
