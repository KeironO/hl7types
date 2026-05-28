"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: CQU_I19
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

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
from ..segments.ERR import ERR
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.NK1 import NK1
from ..segments.REL import REL
from ..segments.RF1 import RF1
from ..segments.SFT import SFT
from ..segments.UAC import UAC

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


class CQU_I19(BaseModel):
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
        default=...,
        title="MSH",
        description="Required",
    )

    SFT: list[_SFT] | None = Field(
        default=None,
        title="SFT",
        description="Optional, repeating",
    )

    UAC: _UAC | None = Field(
        default=None,
        title="UAC",
        description="Optional",
    )

    MSA: _MSA = Field(
        default=...,
        title="MSA",
        description="Required",
    )

    ERR: list[_ERR] | None = Field(
        default=None,
        title="ERR",
        description="Optional, repeating",
    )

    RF1: _RF1 = Field(
        default=...,
        title="RF1",
        description="Required",
    )

    PROVIDER_CONTACT: list[_CQU_I19_PROVIDER_CONTACT] | None = Field(
        default=None,
        title="PROVIDER_CONTACT",
        description="Optional, repeating",
    )

    PATIENT: list[_CQU_I19_PATIENT] | None = Field(
        default=None,
        title="PATIENT",
        description="Optional, repeating",
    )

    NK1: list[_NK1] | None = Field(
        default=None,
        title="NK1",
        description="Optional, repeating",
    )

    INSURANCE: list[_CQU_I19_INSURANCE] | None = Field(
        default=None,
        title="INSURANCE",
        description="Optional, repeating",
    )

    APPOINTMENT_HISTORY: list[_CQU_I19_APPOINTMENT_HISTORY] | None = Field(
        default=None,
        title="APPOINTMENT_HISTORY",
        description="Optional, repeating",
    )

    CLINICAL_HISTORY: list[_CQU_I19_CLINICAL_HISTORY] | None = Field(
        default=None,
        title="CLINICAL_HISTORY",
        description="Optional, repeating",
    )

    PATIENT_VISITS: list[_CQU_I19_PATIENT_VISITS] = Field(
        default=...,
        title="PATIENT_VISITS",
        description="Required, repeating",
    )

    MEDICATION_HISTORY: list[_CQU_I19_MEDICATION_HISTORY] | None = Field(
        default=None,
        title="MEDICATION_HISTORY",
        description="Optional, repeating",
    )

    PROBLEM: list[_CQU_I19_PROBLEM] | None = Field(
        default=None,
        title="PROBLEM",
        description="Optional, repeating",
    )

    GOAL: list[_CQU_I19_GOAL] | None = Field(
        default=None,
        title="GOAL",
        description="Optional, repeating",
    )

    PATHWAY: list[_CQU_I19_PATHWAY] | None = Field(
        default=None,
        title="PATHWAY",
        description="Optional, repeating",
    )

    REL: list[_REL] | None = Field(
        default=None,
        title="REL",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
