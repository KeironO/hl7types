"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: CCM_I21
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH
from ..segments.NK1 import NK1
from ..segments.PD1 import PD1
from ..segments.PID import PID
from ..segments.REL import REL
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.CCM_I21_APPOINTMENT_HISTORY import CCM_I21_APPOINTMENT_HISTORY
from ..groups.CCM_I21_CLINICAL_HISTORY import CCM_I21_CLINICAL_HISTORY
from ..groups.CCM_I21_GOAL import CCM_I21_GOAL
from ..groups.CCM_I21_INSURANCE import CCM_I21_INSURANCE
from ..groups.CCM_I21_MEDICATION_HISTORY import CCM_I21_MEDICATION_HISTORY
from ..groups.CCM_I21_PATHWAY import CCM_I21_PATHWAY
from ..groups.CCM_I21_PATIENT_VISITS import CCM_I21_PATIENT_VISITS
from ..groups.CCM_I21_PROBLEM import CCM_I21_PROBLEM

_CCM_I21_APPOINTMENT_HISTORY = CCM_I21_APPOINTMENT_HISTORY
_CCM_I21_CLINICAL_HISTORY = CCM_I21_CLINICAL_HISTORY
_CCM_I21_GOAL = CCM_I21_GOAL
_CCM_I21_INSURANCE = CCM_I21_INSURANCE
_CCM_I21_MEDICATION_HISTORY = CCM_I21_MEDICATION_HISTORY
_CCM_I21_PATHWAY = CCM_I21_PATHWAY
_CCM_I21_PATIENT_VISITS = CCM_I21_PATIENT_VISITS
_CCM_I21_PROBLEM = CCM_I21_PROBLEM
_MSH = MSH
_NK1 = NK1
_PD1 = PD1
_PID = PID
_REL = REL
_SFT = SFT
_UAC = UAC


class CCM_I21(HL7Model):
    """HL7 v2 CCM_I21 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        PID (PID): required
        PD1 (Optional[PD1]): optional
        NK1 (Optional[List[NK1]]): optional
        INSURANCE (Optional[List[CCM_I21_INSURANCE]]): optional
        APPOINTMENT_HISTORY (Optional[List[CCM_I21_APPOINTMENT_HISTORY]]): optional
        CLINICAL_HISTORY (Optional[List[CCM_I21_CLINICAL_HISTORY]]): optional
        PATIENT_VISITS (List[CCM_I21_PATIENT_VISITS]): required
        MEDICATION_HISTORY (Optional[List[CCM_I21_MEDICATION_HISTORY]]): optional
        PROBLEM (Optional[List[CCM_I21_PROBLEM]]): optional
        GOAL (Optional[List[CCM_I21_GOAL]]): optional
        PATHWAY (Optional[List[CCM_I21_PATHWAY]]): optional
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

    PID: _PID = Field(
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

    INSURANCE: Optional[List[_CCM_I21_INSURANCE]] = Field(
        default=None,
        title="INSURANCE",
        description="Optional, repeating",
    )

    APPOINTMENT_HISTORY: Optional[List[_CCM_I21_APPOINTMENT_HISTORY]] = Field(
        default=None,
        title="APPOINTMENT_HISTORY",
        description="Optional, repeating",
    )

    CLINICAL_HISTORY: Optional[List[_CCM_I21_CLINICAL_HISTORY]] = Field(
        default=None,
        title="CLINICAL_HISTORY",
        description="Optional, repeating",
    )

    PATIENT_VISITS: List[_CCM_I21_PATIENT_VISITS] = Field(
        min_length=1,
        title="PATIENT_VISITS",
        description="Required, repeating",
    )

    MEDICATION_HISTORY: Optional[List[_CCM_I21_MEDICATION_HISTORY]] = Field(
        default=None,
        title="MEDICATION_HISTORY",
        description="Optional, repeating",
    )

    PROBLEM: Optional[List[_CCM_I21_PROBLEM]] = Field(
        default=None,
        title="PROBLEM",
        description="Optional, repeating",
    )

    GOAL: Optional[List[_CCM_I21_GOAL]] = Field(
        default=None,
        title="GOAL",
        description="Optional, repeating",
    )

    PATHWAY: Optional[List[_CCM_I21_PATHWAY]] = Field(
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
