"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: VXR_V03
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

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


class VXR_V03(HL7Model):
    """VXR - Vaccination record response.

    Attributes:
        MSH (MSH): MSH - message header segment, required
        MSA (MSA): MSA - message acknowledgment segment, required
        QRD (QRD): QRD - original-style query definition segment, required
        QRF (Optional[QRF]): QRF - original style query filter segment, optional
        PID (PID): PID - patient identification segment, required
        PD1 (Optional[PD1]): PD1 - patient additional demographic segment, optional
        NK1 (Optional[List[NK1]]): NK1 - next of kin / associated parties segment-, optional
        PATIENT_VISIT (Optional[VXR_V03_PATIENT_VISIT]): optional
        INSURANCE (Optional[List[VXR_V03_INSURANCE]]): optional
        ORDER (Optional[List[VXR_V03_ORDER]]): optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="MSH - message header segment",
    )

    MSA: _MSA = Field(
        title="MSA",
        description="MSA - message acknowledgment segment",
    )

    QRD: _QRD = Field(
        title="QRD",
        description="QRD - original-style query definition segment",
    )

    QRF: Optional[_QRF] = Field(
        default=None,
        title="QRF",
        description="QRF - original style query filter segment",
    )

    PID: _PID = Field(
        title="PID",
        description="PID - patient identification segment",
    )

    PD1: Optional[_PD1] = Field(
        default=None,
        title="PD1",
        description="PD1 - patient additional demographic segment",
    )

    NK1: Optional[List[_NK1]] = Field(
        default=None,
        title="NK1",
        description="NK1 - next of kin / associated parties segment-",
    )

    PATIENT_VISIT: Optional[_VXR_V03_PATIENT_VISIT] = Field(
        default=None,
        title="PATIENT_VISIT",
    )

    INSURANCE: Optional[List[_VXR_V03_INSURANCE]] = Field(
        default=None,
        title="INSURANCE",
    )

    ORDER: Optional[List[_VXR_V03_ORDER]] = Field(
        default=None,
        title="ORDER",
    )

    model_config = ConfigDict(populate_by_name=True)
