"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: VXR_V03
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.VXR_V03_INSURANCE import VXR_V03_INSURANCE
from ..groups.VXR_V03_ORDER import VXR_V03_ORDER
from ..groups.VXR_V03_PATIENT_VISIT import VXR_V03_PATIENT_VISIT
from ..segments.GT1 import GT1
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.NK1 import NK1
from ..segments.PD1 import PD1
from ..segments.PID import PID
from ..segments.QRD import QRD
from ..segments.QRF import QRF
from ..segments.SFT import SFT
from ..segments.UAC import UAC

_GT1 = GT1
_MSA = MSA
_MSH = MSH
_NK1 = NK1
_PD1 = PD1
_PID = PID
_QRD = QRD
_QRF = QRF
_SFT = SFT
_UAC = UAC
_VXR_V03_INSURANCE = VXR_V03_INSURANCE
_VXR_V03_ORDER = VXR_V03_ORDER
_VXR_V03_PATIENT_VISIT = VXR_V03_PATIENT_VISIT


class VXR_V03(BaseModel):
    """HL7 v2 VXR_V03 message.

    Attributes:
        MSH (MSH): required
        MSA (MSA): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
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

    QRD: _QRD = Field(
        default=...,
        title="QRD",
        description="Required",
    )

    QRF: _QRF | None = Field(
        default=None,
        title="QRF",
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

    PATIENT_VISIT: _VXR_V03_PATIENT_VISIT | None = Field(
        default=None,
        title="PATIENT_VISIT",
        description="Optional",
    )

    GT1: list[_GT1] | None = Field(
        default=None,
        title="GT1",
        description="Optional, repeating",
    )

    INSURANCE: list[_VXR_V03_INSURANCE] | None = Field(
        default=None,
        title="INSURANCE",
        description="Optional, repeating",
    )

    ORDER: list[_VXR_V03_ORDER] | None = Field(
        default=None,
        title="ORDER",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
