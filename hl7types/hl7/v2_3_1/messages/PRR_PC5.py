"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: PRR_PC5
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.PRR_PC5_PATIENT import PRR_PC5_PATIENT
from ..segments.ERR import ERR
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.QAK import QAK
from ..segments.QRD import QRD

_ERR = ERR
_MSA = MSA
_MSH = MSH
_PRR_PC5_PATIENT = PRR_PC5_PATIENT
_QAK = QAK
_QRD = QRD


class PRR_PC5(BaseModel):
    """HL7 v2 PRR_PC5 message.

    Attributes:
        MSH (MSH): required
        MSA (MSA): required
        ERR (Optional[ERR]): optional
        QAK (Optional[QAK]): optional
        QRD (QRD): required
        PATIENT (List[PRR_PC5_PATIENT]): required
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

    PATIENT: list[_PRR_PC5_PATIENT] = Field(
        default=...,
        title="PATIENT",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
