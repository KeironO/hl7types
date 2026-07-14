"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: VXX_V02
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
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
    """VXX - Response to vaccination query returning multiple PID matches.

    Attributes:
        MSH (MSH): Message header segment, required
        MSA (MSA): Message acknowledgement segment, required
        QRD (QRD): Query definition segment, required
        QRF (Optional[QRF]): Query filter segment, optional
        PATIENT (List[VXX_V02_PATIENT]): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message header segment",
    )

    MSA: _MSA = Field(
        title="MSA",
        description="Message acknowledgement segment",
    )

    QRD: _QRD = Field(
        title="QRD",
        description="Query definition segment",
    )

    QRF: Optional[_QRF] = Field(
        default=None,
        title="QRF",
        description="Query filter segment",
    )

    PATIENT: List[_VXX_V02_PATIENT] = Field(
        min_length=1,
        title="PATIENT",
    )

    model_config = {"populate_by_name": True}
