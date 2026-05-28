"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: CCI_I22
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

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


class CCI_I22(BaseModel):
    """HL7 v2 CCI_I22 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        MSA (MSA): required
        ERR (Optional[List[ERR]]): optional
        PID (PID): required
        PD1 (Optional[PD1]): optional
        NK1 (Optional[List[NK1]]): optional
        INSURANCE (Optional[List[CCI_I22_INSURANCE]]): optional
        APPOINTMENT_HISTORY (Optional[List[CCI_I22_APPOINTMENT_HISTORY]]): optional
        CLINICAL_HISTORY (Optional[List[CCI_I22_CLINICAL_HISTORY]]): optional
        PATIENT_VISITS (List[CCI_I22_PATIENT_VISITS]): required
        MEDICATION_HISTORY (Optional[List[CCI_I22_MEDICATION_HISTORY]]): optional
        PROBLEM (Optional[List[CCI_I22_PROBLEM]]): optional
        GOAL (Optional[List[CCI_I22_GOAL]]): optional
        PATHWAY (Optional[List[CCI_I22_PATHWAY]]): optional
        REL (Optional[List[REL]]): optional
    """

    MSH: _MSH = Field(
        default=...,
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
        default=...,
        title="MSA",
        description="Required",
    )

    ERR: Optional[List[_ERR]] = Field(
        default=None,
        title="ERR",
        description="Optional, repeating",
    )

    PID: _PID = Field(
        default=...,
        title="PID",
        description="Required",
    )

    PD1: Optional[_PD1] = Field(
        default=None,
        title="PD1",
        description="Optional",
    )

    NK1: Optional[List[_NK1]] = Field(
        default=None,
        title="NK1",
        description="Optional, repeating",
    )

    INSURANCE: Optional[List[_CCI_I22_INSURANCE]] = Field(
        default=None,
        title="INSURANCE",
        description="Optional, repeating",
    )

    APPOINTMENT_HISTORY: Optional[List[_CCI_I22_APPOINTMENT_HISTORY]] = Field(
        default=None,
        title="APPOINTMENT_HISTORY",
        description="Optional, repeating",
    )

    CLINICAL_HISTORY: Optional[List[_CCI_I22_CLINICAL_HISTORY]] = Field(
        default=None,
        title="CLINICAL_HISTORY",
        description="Optional, repeating",
    )

    PATIENT_VISITS: List[_CCI_I22_PATIENT_VISITS] = Field(
        default=...,
        title="PATIENT_VISITS",
        description="Required, repeating",
    )

    MEDICATION_HISTORY: Optional[List[_CCI_I22_MEDICATION_HISTORY]] = Field(
        default=None,
        title="MEDICATION_HISTORY",
        description="Optional, repeating",
    )

    PROBLEM: Optional[List[_CCI_I22_PROBLEM]] = Field(
        default=None,
        title="PROBLEM",
        description="Optional, repeating",
    )

    GOAL: Optional[List[_CCI_I22_GOAL]] = Field(
        default=None,
        title="GOAL",
        description="Optional, repeating",
    )

    PATHWAY: Optional[List[_CCI_I22_PATHWAY]] = Field(
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
