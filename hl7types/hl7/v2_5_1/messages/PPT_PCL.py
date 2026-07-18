"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: PPT_PCL
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
from ..segments.SFT import SFT

from ..groups.PPT_PCL_PATIENT import PPT_PCL_PATIENT

_ERR = ERR
_MSA = MSA
_MSH = MSH
_PPT_PCL_PATIENT = PPT_PCL_PATIENT
_QAK = QAK
_QRD = QRD
_SFT = SFT


class PPT_PCL(HL7Model):
    """PPT - PC/ pathway (goal-oriented) query response (S12.3.12).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        MSA (MSA): Message Acknowledgment, required
        ERR (Optional[List[ERR]]): Error, optional
        QAK (Optional[QAK]): Query Acknowledgment, optional
        QRD (QRD): Original-Style Query Definition, required
        PATIENT (List[PPT_PCL_PATIENT]): required
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
        description="Original-Style Query Definition",
    )

    PATIENT: List[_PPT_PCL_PATIENT] = Field(
        min_length=1,
        title="PATIENT",
    )

    model_config = ConfigDict(populate_by_name=True)
