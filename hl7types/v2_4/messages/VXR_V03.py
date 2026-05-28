"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: VXR_V03
Type: Message
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.GT1 import GT1
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.NK1 import NK1
from ..segments.PD1 import PD1
from ..segments.PID import PID
from ..segments.QRD import QRD
from ..segments.QRF import QRF

from ..groups.VXR_V03_INSURANCE import VXR_V03_INSURANCE
from ..groups.VXR_V03_ORDER import VXR_V03_ORDER
from ..groups.VXR_V03_PATIENT_VISIT import VXR_V03_PATIENT_VISIT

_GT1 = GT1
_MSA = MSA
_MSH = MSH
_NK1 = NK1
_PD1 = PD1
_PID = PID
_QRD = QRD
_QRF = QRF
_VXR_V03_INSURANCE = VXR_V03_INSURANCE
_VXR_V03_ORDER = VXR_V03_ORDER
_VXR_V03_PATIENT_VISIT = VXR_V03_PATIENT_VISIT


class VXR_V03(BaseModel):
    """HL7 v2 VXR_V03 message.

    Attributes:
        MSH (MSH): required
        MSA (MSA): required
        QRD (QRD): required
        QRF (Optional[QRF]): optional
        PID (PID): required
        PD1 (Optional[PD1]): optional
        NK1 (Optional[List[NK1]]): optional
        PATIENT_VISIT (Optional[VXR_V03_PATIENT_VISIT]): optional
        GT1 (Optional[List[GT1]]): optional
        INSURANCE (Optional[List[VXR_V03_INSURANCE]]): optional
        ORDER (Optional[List[VXR_V03_ORDER]]): optional
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    MSA: _MSA = Field(
        default=...,
        title="MSA",
        description="Required",
    )

    QRD: _QRD = Field(
        default=...,
        title="QRD",
        description="Required",
    )

    QRF: Optional[_QRF] = Field(
        default=None,
        title="QRF",
        description="Optional",
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

    PATIENT_VISIT: Optional[_VXR_V03_PATIENT_VISIT] = Field(
        default=None,
        title="PATIENT_VISIT",
        description="Optional",
    )

    GT1: Optional[List[_GT1]] = Field(
        default=None,
        title="GT1",
        description="Optional, repeating",
    )

    INSURANCE: Optional[List[_VXR_V03_INSURANCE]] = Field(
        default=None,
        title="INSURANCE",
        description="Optional, repeating",
    )

    ORDER: Optional[List[_VXR_V03_ORDER]] = Field(
        default=None,
        title="ORDER",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
