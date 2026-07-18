"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: PTR_PCF
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

from ..groups.PTR_PCF_PATIENT import PTR_PCF_PATIENT

_ERR = ERR
_MSA = MSA
_MSH = MSH
_PTR_PCF_PATIENT = PTR_PCF_PATIENT
_QAK = QAK
_QRD = QRD


class PTR_PCF(HL7Model):
    """PTR - PC/ Pathway (Problem-Oriented) Query Response.

    Attributes:
        MSH (MSH): MSH - message header segment, required
        MSA (MSA): MSA - message acknowledgment segment, required
        ERR (Optional[ERR]): ERR - error segment, optional
        QAK (Optional[QAK]): Query Acknowledgement, optional
        QRD (QRD): QRD - original-style query definition segment, required
        PATIENT (List[PTR_PCF_PATIENT]): required
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

    PATIENT: List[_PTR_PCF_PATIENT] = Field(
        min_length=1,
        title="PATIENT",
    )

    model_config = ConfigDict(populate_by_name=True)
