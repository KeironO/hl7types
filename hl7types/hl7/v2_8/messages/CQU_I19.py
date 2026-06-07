"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: CQU_I19
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
    """HL7 v2 CQU_I19 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        MSA (MSA): required
        ERR (Optional[List[ERR]]): optional
        RF1 (RF1): required
        PROVIDER_CONTACT (Optional[List[CQU_I19_PROVIDER_CONTACT]]): optional
        PATIENT (Optional[List[CQU_I19_PATIENT]]): optional
        NK1 (Optional[List[NK1]]): optional
        INSURANCE (Optional[List[CQU_I19_INSURANCE]]): optional
        APPOINTMENT_HISTORY (Optional[List[CQU_I19_APPOINTMENT_HISTORY]]): optional
        CLINICAL_HISTORY (Optional[List[CQU_I19_CLINICAL_HISTORY]]): optional
        PATIENT_VISITS (List[CQU_I19_PATIENT_VISITS]): required
        MEDICATION_HISTORY (Optional[List[CQU_I19_MEDICATION_HISTORY]]): optional
        PROBLEM (Optional[List[CQU_I19_PROBLEM]]): optional
        GOAL (Optional[List[CQU_I19_GOAL]]): optional
        PATHWAY (Optional[List[CQU_I19_PATHWAY]]): optional
        REL (Optional[List[REL]]): optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Required",
    )

    SFT: Optional[List[_SFT]] = Field(
        default=None,
        title="SFT",
        description="Optional, repeating",
    )

    UAC: Optional[_UAC] = Field(
        default=None,
        title="UAC",
        description="Optional",
    )

    MSA: _MSA = Field(
        title="MSA",
        description="Required",
    )

    ERR: Optional[List[_ERR]] = Field(
        default=None,
        title="ERR",
        description="Optional, repeating",
    )

    RF1: _RF1 = Field(
        title="RF1",
        description="Required",
    )

    PROVIDER_CONTACT: Optional[List[_CQU_I19_PROVIDER_CONTACT]] = Field(
        default=None,
        title="PROVIDER_CONTACT",
        description="Optional, repeating",
    )

    PATIENT: Optional[List[_CQU_I19_PATIENT]] = Field(
        default=None,
        title="PATIENT",
        description="Optional, repeating",
    )

    NK1: Optional[List[_NK1]] = Field(
        default=None,
        title="NK1",
        description="Optional, repeating",
    )

    INSURANCE: Optional[List[_CQU_I19_INSURANCE]] = Field(
        default=None,
        title="INSURANCE",
        description="Optional, repeating",
    )

    APPOINTMENT_HISTORY: Optional[List[_CQU_I19_APPOINTMENT_HISTORY]] = Field(
        default=None,
        title="APPOINTMENT_HISTORY",
        description="Optional, repeating",
    )

    CLINICAL_HISTORY: Optional[List[_CQU_I19_CLINICAL_HISTORY]] = Field(
        default=None,
        title="CLINICAL_HISTORY",
        description="Optional, repeating",
    )

    PATIENT_VISITS: List[_CQU_I19_PATIENT_VISITS] = Field(
        min_length=1,
        title="PATIENT_VISITS",
        description="Required, repeating",
    )

    MEDICATION_HISTORY: Optional[List[_CQU_I19_MEDICATION_HISTORY]] = Field(
        default=None,
        title="MEDICATION_HISTORY",
        description="Optional, repeating",
    )

    PROBLEM: Optional[List[_CQU_I19_PROBLEM]] = Field(
        default=None,
        title="PROBLEM",
        description="Optional, repeating",
    )

    GOAL: Optional[List[_CQU_I19_GOAL]] = Field(
        default=None,
        title="GOAL",
        description="Optional, repeating",
    )

    PATHWAY: Optional[List[_CQU_I19_PATHWAY]] = Field(
        default=None,
        title="PATHWAY",
        description="Optional, repeating",
    )

    REL: Optional[List[_REL]] = Field(
        default=None,
        title="REL",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
