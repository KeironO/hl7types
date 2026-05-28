"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: VXU_V04
Type: Message
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.GT1 import GT1
from ..segments.MSH import MSH
from ..segments.NK1 import NK1
from ..segments.PD1 import PD1
from ..segments.PID import PID
from ..segments.SFT import SFT

from ..groups.VXU_V04_INSURANCE import VXU_V04_INSURANCE
from ..groups.VXU_V04_ORDER import VXU_V04_ORDER
from ..groups.VXU_V04_PATIENT import VXU_V04_PATIENT

_GT1 = GT1
_MSH = MSH
_NK1 = NK1
_PD1 = PD1
_PID = PID
_SFT = SFT
_VXU_V04_INSURANCE = VXU_V04_INSURANCE
_VXU_V04_ORDER = VXU_V04_ORDER
_VXU_V04_PATIENT = VXU_V04_PATIENT


class VXU_V04(BaseModel):
    """HL7 v2 VXU_V04 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        PID (PID): required
        PD1 (Optional[PD1]): optional
        NK1 (Optional[List[NK1]]): optional
        PATIENT (Optional[VXU_V04_PATIENT]): optional
        GT1 (Optional[List[GT1]]): optional
        INSURANCE (Optional[List[VXU_V04_INSURANCE]]): optional
        ORDER (Optional[List[VXU_V04_ORDER]]): optional
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

    PATIENT: Optional[_VXU_V04_PATIENT] = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    GT1: Optional[List[_GT1]] = Field(
        default=None,
        title="GT1",
        description="Optional, repeating",
    )

    INSURANCE: Optional[List[_VXU_V04_INSURANCE]] = Field(
        default=None,
        title="INSURANCE",
        description="Optional, repeating",
    )

    ORDER: Optional[List[_VXU_V04_ORDER]] = Field(
        default=None,
        title="ORDER",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
