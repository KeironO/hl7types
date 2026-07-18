"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
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
    """PRR - PC/ Problem Response.

    Attributes:
        MSH (MSH): MSH - message header segment, required
        MSA (MSA): MSA - message acknowledgment segment, required
        ERR (Optional[ERR]): ERR - error segment, optional
        QAK (Optional[QAK]): Query Acknowledgement, optional
        QRD (QRD): QRD - original-style query definition segment, required
        PATIENT (List[PRR_PC5_PATIENT]): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="MSH - message header segment",
    )

    MSA: _MSA = Field(
        title="MSA",
        description="MSA - message acknowledgment segment",
    )

    ERR: Optional[_ERR] = Field(
        default=None,
        title="ERR",
        description="ERR - error segment",
    )

    QAK: Optional[_QAK] = Field(
        default=None,
        title="QAK",
        description="Query Acknowledgement",
    )

    QRD: _QRD = Field(
        title="QRD",
        description="QRD - original-style query definition segment",
    )

    PATIENT: List[_PRR_PC5_PATIENT] = Field(
        min_length=1,
        title="PATIENT",
    )

    model_config = ConfigDict(populate_by_name=True)
