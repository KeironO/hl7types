"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: PTR_PCF
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.PTR_PCF_PATIENT import PTR_PCF_PATIENT
from ..segments.ERR import ERR
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.QAK import QAK
from ..segments.QRD import QRD

_ERR = ERR
_MSA = MSA
_MSH = MSH
_PTR_PCF_PATIENT = PTR_PCF_PATIENT
_QAK = QAK
_QRD = QRD


class PTR_PCF(BaseModel):
    """HL7 v2 PTR_PCF message.

    Attributes:
        MSH (MSH): required
        MSA (MSA): required
        ERR (Optional[ERR]): optional
        QAK (Optional[QAK]): optional
        QRD (QRD): required
        PATIENT (List[PTR_PCF_PATIENT]): required
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

    ERR: _ERR | None = Field(
        default=None,
        title="ERR",
        description="Optional",
    )

    QAK: _QAK | None = Field(
        default=None,
        title="QAK",
        description="Optional",
    )

    QRD: _QRD = Field(
        default=...,
        title="QRD",
        description="Required",
    )

    PATIENT: list[_PTR_PCF_PATIENT] = Field(
        default=...,
        title="PATIENT",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
