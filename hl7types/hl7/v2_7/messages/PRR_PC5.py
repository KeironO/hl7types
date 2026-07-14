"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: PRR_PC5
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
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.PRR_PC5_PATIENT import PRR_PC5_PATIENT

_ERR = ERR
_MSA = MSA
_MSH = MSH
_PRR_PC5_PATIENT = PRR_PC5_PATIENT
_QAK = QAK
_QRD = QRD
_SFT = SFT
_UAC = UAC


class PRR_PC5(HL7Model):
    """PRR - PC/ problem response (S12.3.6).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        MSA (MSA): Message Acknowledgment, required
        ERR (Optional[List[ERR]]): Error, optional
        QAK (Optional[QAK]): Query Acknowledgment, optional
        QRD (QRD): withdrawn, required
        PATIENT (List[PRR_PC5_PATIENT]): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message Header",
    )

    SFT: Optional[List[_SFT]] = Field(
        default=None,
        title="SFT",
        description="Software Segment",
    )

    UAC: Optional[_UAC] = Field(
        default=None,
        title="UAC",
        description="User Authentication Credential Segment",
    )

    MSA: _MSA = Field(
        title="MSA",
        description="Message Acknowledgment",
    )

    ERR: Optional[List[_ERR]] = Field(
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
        description="withdrawn",
    )

    PATIENT: List[_PRR_PC5_PATIENT] = Field(
        min_length=1,
        title="PATIENT",
    )

    model_config = {"populate_by_name": True}
