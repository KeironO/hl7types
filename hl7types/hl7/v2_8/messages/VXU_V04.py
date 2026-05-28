"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: VXU_V04
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.VXU_V04_INSURANCE import VXU_V04_INSURANCE
from ..groups.VXU_V04_ORDER import VXU_V04_ORDER
from ..groups.VXU_V04_PATIENT_VISIT import VXU_V04_PATIENT_VISIT
from ..groups.VXU_V04_PERSON_OBSERVATION import VXU_V04_PERSON_OBSERVATION
from ..segments.ARV import ARV
from ..segments.GT1 import GT1
from ..segments.MSH import MSH
from ..segments.NK1 import NK1
from ..segments.PD1 import PD1
from ..segments.PID import PID
from ..segments.SFT import SFT
from ..segments.UAC import UAC

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


class VXU_V04(BaseModel):
    """HL7 v2 VXU_V04 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        PID (PID): required
        PD1 (Optional[PD1]): optional
        NK1 (Optional[List[NK1]]): optional
        ARV (Optional[List[ARV]]): optional
        PATIENT_VISIT (Optional[VXU_V04_PATIENT_VISIT]): optional
        GT1 (Optional[List[GT1]]): optional
        INSURANCE (Optional[List[VXU_V04_INSURANCE]]): optional
        PERSON_OBSERVATION (Optional[List[VXU_V04_PERSON_OBSERVATION]]): optional
        ORDER (Optional[List[VXU_V04_ORDER]]): optional
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

    PID: _PID = Field(
        default=...,
        title="PID",
        description="Required",
    )

    PD1: _PD1 | None = Field(
        default=None,
        title="PD1",
        description="Optional",
    )

    NK1: list[_NK1] | None = Field(
        default=None,
        title="NK1",
        description="Optional, repeating",
    )

    ARV: list[_ARV] | None = Field(
        default=None,
        title="ARV",
        description="Optional, repeating",
    )

    PATIENT_VISIT: _VXU_V04_PATIENT_VISIT | None = Field(
        default=None,
        title="PATIENT_VISIT",
        description="Optional",
    )

    GT1: list[_GT1] | None = Field(
        default=None,
        title="GT1",
        description="Optional, repeating",
    )

    INSURANCE: list[_VXU_V04_INSURANCE] | None = Field(
        default=None,
        title="INSURANCE",
        description="Optional, repeating",
    )

    PERSON_OBSERVATION: list[_VXU_V04_PERSON_OBSERVATION] | None = Field(
        default=None,
        title="PERSON_OBSERVATION",
        description="Optional, repeating",
    )

    ORDER: list[_VXU_V04_ORDER] | None = Field(
        default=None,
        title="ORDER",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
