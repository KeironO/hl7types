"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: CCR_I16
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

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
from ..segments.MSH import MSH
from ..segments.NK1 import NK1
from ..segments.REL import REL
from ..segments.RF1 import RF1
from ..segments.SFT import SFT
from ..segments.UAC import UAC

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


class CCR_I16(BaseModel):
    """HL7 v2 CCR_I16 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        RF1 (List[RF1]): required
        PROVIDER_CONTACT (List[CCR_I16_PROVIDER_CONTACT]): required
        CLINICAL_ORDER (Optional[List[CCR_I16_CLINICAL_ORDER]]): optional
        PATIENT (List[CCR_I16_PATIENT]): required
        NK1 (Optional[List[NK1]]): optional
        INSURANCE (Optional[List[CCR_I16_INSURANCE]]): optional
        APPOINTMENT_HISTORY (Optional[List[CCR_I16_APPOINTMENT_HISTORY]]): optional
        CLINICAL_HISTORY (Optional[List[CCR_I16_CLINICAL_HISTORY]]): optional
        PATIENT_VISITS (List[CCR_I16_PATIENT_VISITS]): required
        MEDICATION_HISTORY (Optional[List[CCR_I16_MEDICATION_HISTORY]]): optional
        PROBLEM (Optional[List[CCR_I16_PROBLEM]]): optional
        GOAL (Optional[List[CCR_I16_GOAL]]): optional
        PATHWAY (Optional[List[CCR_I16_PATHWAY]]): optional
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

    RF1: list[_RF1] = Field(
        default=...,
        title="RF1",
        description="Required, repeating",
    )

    PROVIDER_CONTACT: list[_CCR_I16_PROVIDER_CONTACT] = Field(
        default=...,
        title="PROVIDER_CONTACT",
        description="Required, repeating",
    )

    CLINICAL_ORDER: list[_CCR_I16_CLINICAL_ORDER] | None = Field(
        default=None,
        title="CLINICAL_ORDER",
        description="Optional, repeating",
    )

    PATIENT: list[_CCR_I16_PATIENT] = Field(
        default=...,
        title="PATIENT",
        description="Required, repeating",
    )

    NK1: list[_NK1] | None = Field(
        default=None,
        title="NK1",
        description="Optional, repeating",
    )

    INSURANCE: list[_CCR_I16_INSURANCE] | None = Field(
        default=None,
        title="INSURANCE",
        description="Optional, repeating",
    )

    APPOINTMENT_HISTORY: list[_CCR_I16_APPOINTMENT_HISTORY] | None = Field(
        default=None,
        title="APPOINTMENT_HISTORY",
        description="Optional, repeating",
    )

    CLINICAL_HISTORY: list[_CCR_I16_CLINICAL_HISTORY] | None = Field(
        default=None,
        title="CLINICAL_HISTORY",
        description="Optional, repeating",
    )

    PATIENT_VISITS: list[_CCR_I16_PATIENT_VISITS] = Field(
        default=...,
        title="PATIENT_VISITS",
        description="Required, repeating",
    )

    MEDICATION_HISTORY: list[_CCR_I16_MEDICATION_HISTORY] | None = Field(
        default=None,
        title="MEDICATION_HISTORY",
        description="Optional, repeating",
    )

    PROBLEM: list[_CCR_I16_PROBLEM] | None = Field(
        default=None,
        title="PROBLEM",
        description="Optional, repeating",
    )

    GOAL: list[_CCR_I16_GOAL] | None = Field(
        default=None,
        title="GOAL",
        description="Optional, repeating",
    )

    PATHWAY: list[_CCR_I16_PATHWAY] | None = Field(
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
