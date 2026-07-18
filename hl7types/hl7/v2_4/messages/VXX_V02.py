"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: VXX_V02
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.QRD import QRD
from ..segments.QRF import QRF

from ..groups.VXX_V02_PATIENT import VXX_V02_PATIENT

_MSA = MSA
_MSH = MSH
_QRD = QRD
_QRF = QRF
_VXX_V02_PATIENT = VXX_V02_PATIENT


class VXX_V02(HL7Model):
    """VXX - Response to vaccination query returning multiple PID matches (S4).

    Attributes:
        MSH (MSH): Message Header, required
        MSA (MSA): Message Acknowledgment, required
        QRD (QRD): Original-Style Query Definition, required
        QRF (Optional[QRF]): Original Style Query Filter, optional
        PATIENT (List[VXX_V02_PATIENT]): required
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

    PATIENT: List[_VXX_V02_PATIENT] = Field(
        min_length=1,
        title="PATIENT",
    )

    model_config = ConfigDict(populate_by_name=True)
