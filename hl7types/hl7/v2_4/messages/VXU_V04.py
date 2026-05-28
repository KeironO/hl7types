"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: VXU_V04
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.VXU_V04_INSURANCE import VXU_V04_INSURANCE
from ..groups.VXU_V04_ORDER import VXU_V04_ORDER
from ..groups.VXU_V04_PATIENT import VXU_V04_PATIENT
from ..segments.GT1 import GT1
from ..segments.MSH import MSH
from ..segments.NK1 import NK1
from ..segments.PD1 import PD1
from ..segments.PID import PID

_GT1 = GT1
_MSH = MSH
_NK1 = NK1
_PD1 = PD1
_PID = PID
_VXU_V04_INSURANCE = VXU_V04_INSURANCE
_VXU_V04_ORDER = VXU_V04_ORDER
_VXU_V04_PATIENT = VXU_V04_PATIENT


class VXU_V04(BaseModel):
    """HL7 v2 VXU_V04 message.

    Attributes:
        MSH (MSH): required
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

    PATIENT: _VXU_V04_PATIENT | None = Field(
        default=None,
        title="PATIENT",
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

    ORDER: list[_VXU_V04_ORDER] | None = Field(
        default=None,
        title="ORDER",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
