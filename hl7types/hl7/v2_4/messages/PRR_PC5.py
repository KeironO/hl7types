"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: PRR_PC5
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.ERR import ERR
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.QAK import QAK
from ..segments.QRD import QRD

from ..groups.PRR_PC5_PATIENT import PRR_PC5_PATIENT

_ERR = ERR
_MSA = MSA
_MSH = MSH
_PRR_PC5_PATIENT = PRR_PC5_PATIENT
_QAK = QAK
_QRD = QRD


class PRR_PC5(HL7Model):
    """PRR - PC/ Problem Response (S12).

    Attributes:
        MSH (MSH): Message Header, required
        MSA (MSA): Message Acknowledgment, required
        ERR (Optional[ERR]): Error, optional
        QAK (Optional[QAK]): Query Acknowledgment, optional
        QRD (QRD): Original-Style Query Definition, required
        PATIENT (List[PRR_PC5_PATIENT]): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message Header",
    )

    MSA: _MSA = Field(
        title="MSA",
        description="Message Acknowledgment",
    )

    ERR: Optional[_ERR] = Field(
        default=None,
        title="ERR",
        description="Error",
    )

    QAK: Optional[_QAK] = Field(
        default=None,
        title="QAK",
        description="Query Acknowledgment",
    )

    QRD: _QRD = Field(
        title="QRD",
        description="Original-Style Query Definition",
    )

    PATIENT: List[_PRR_PC5_PATIENT] = Field(
        min_length=1,
        title="PATIENT",
    )

    model_config = ConfigDict(populate_by_name=True)
