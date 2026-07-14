"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: VXR_V03
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

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


class VXR_V03(HL7Model):
    """VXR - Vaccination record response (S4).

    Attributes:
        MSH (MSH): Message Header, required
        MSA (MSA): Message Acknowledgment, required
        QRD (QRD): Original-Style Query Definition, required
        QRF (Optional[QRF]): Original Style Query Filter, optional
        PID (PID): Patient identification, required
        PD1 (Optional[PD1]): patient additional demographic, optional
        NK1 (Optional[List[NK1]]): Next of kin / associated parties, optional
        PATIENT_VISIT (Optional[VXR_V03_PATIENT_VISIT]): optional
        GT1 (Optional[List[GT1]]): Guarantor, optional
        INSURANCE (Optional[List[VXR_V03_INSURANCE]]): optional
        ORDER (Optional[List[VXR_V03_ORDER]]): optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message Header",
    )

    MSA: _MSA = Field(
        title="MSA",
        description="Message Acknowledgment",
    )

    QRD: _QRD = Field(
        title="QRD",
        description="Original-Style Query Definition",
    )

    QRF: Optional[_QRF] = Field(
        default=None,
        title="QRF",
        description="Original Style Query Filter",
    )

    PID: _PID = Field(
        title="PID",
        description="Patient identification",
    )

    PD1: Optional[_PD1] = Field(
        default=None,
        title="PD1",
        description="patient additional demographic",
    )

    NK1: Optional[List[_NK1]] = Field(
        default=None,
        title="NK1",
        description="Next of kin / associated parties",
    )

    PATIENT_VISIT: Optional[_VXR_V03_PATIENT_VISIT] = Field(
        default=None,
        title="PATIENT_VISIT",
    )

    GT1: Optional[List[_GT1]] = Field(
        default=None,
        title="GT1",
        description="Guarantor",
    )

    INSURANCE: Optional[List[_VXR_V03_INSURANCE]] = Field(
        default=None,
        title="INSURANCE",
    )

    ORDER: Optional[List[_VXR_V03_ORDER]] = Field(
        default=None,
        title="ORDER",
    )

    model_config = {"populate_by_name": True}
