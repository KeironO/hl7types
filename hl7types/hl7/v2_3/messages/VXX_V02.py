"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: VXX_V02
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.VXX_V02_PATIENT import VXX_V02_PATIENT
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.QRD import QRD
from ..segments.QRF import QRF

_MSA = MSA
_MSH = MSH
_QRD = QRD
_QRF = QRF
_VXX_V02_PATIENT = VXX_V02_PATIENT


class VXX_V02(BaseModel):
    """HL7 v2 VXX_V02 message.

    Attributes:
        MSH (MSH): required
        MSA (MSA): required
        QRD (QRD): required
        QRF (Optional[QRF]): optional
        PATIENT (List[VXX_V02_PATIENT]): required
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

    QRF: _QRF | None = Field(
        default=None,
        title="QRF",
        description="Optional",
    )

    PATIENT: list[_VXX_V02_PATIENT] = Field(
        default=...,
        title="PATIENT",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
