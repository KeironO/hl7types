"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: PTR_PCF
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.ERR import ERR
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.QAK import QAK
from ..segments.QRD import QRD

from ..groups.PTR_PCF_PATIENT import PTR_PCF_PATIENT

_ERR = ERR
_MSA = MSA
_MSH = MSH
_PTR_PCF_PATIENT = PTR_PCF_PATIENT
_QAK = QAK
_QRD = QRD


class PTR_PCF(HL7Model):
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
        title="MSH",
        description="Required",
    )

    MSA: _MSA = Field(
        title="MSA",
        description="Required",
    )

    ERR: Optional[_ERR] = Field(
        default=None,
        title="ERR",
        description="Optional",
    )

    QAK: Optional[_QAK] = Field(
        default=None,
        title="QAK",
        description="Optional",
    )

    QRD: _QRD = Field(
        title="QRD",
        description="Required",
    )

    PATIENT: List[_PTR_PCF_PATIENT] = Field(
        min_length=1,
        title="PATIENT",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
