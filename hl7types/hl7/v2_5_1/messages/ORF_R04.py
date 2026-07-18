"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: ORF_R04
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.DSC import DSC
from ..segments.ERR import ERR
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.QAK import QAK
from ..segments.QRD import QRD
from ..segments.QRF import QRF
from ..segments.SFT import SFT

from ..groups.ORF_R04_PIDNTEORCOBRNTETQ1TQ2CTDOBXNTECTI_SUPPGRP import ORF_R04_PIDNTEORCOBRNTETQ1TQ2CTDOBXNTECTI_SUPPGRP

_DSC = DSC
_ERR = ERR
_MSA = MSA
_MSH = MSH
_ORF_R04_PIDNTEORCOBRNTETQ1TQ2CTDOBXNTECTI_SUPPGRP = ORF_R04_PIDNTEORCOBRNTETQ1TQ2CTDOBXNTECTI_SUPPGRP
_QAK = QAK
_QRD = QRD
_QRF = QRF
_SFT = SFT


class ORF_R04(HL7Model):
    """ORF - Response to query; transmission of requested observation (S7.3.3).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        MSA (MSA): Message Acknowledgment, required
        QRD (QRD): Original-Style Query Definition, required
        QRF (Optional[QRF]): Original style query filter, optional
        PIDNTEORCOBRNTETQ1TQ2CTDOBXNTECTI_SUPPGRP (List[ORF_R04_PIDNTEORCOBRNTETQ1TQ2CTDOBXNTECTI_SUPPGRP]): required
        ERR (Optional[List[ERR]]): Error, optional
        QAK (Optional[QAK]): Query Acknowledgment, optional
        DSC (Optional[DSC]): Continuation Pointer, optional
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

    QRD: _QRD = Field(
        title="QRD",
        description="Original-Style Query Definition",
    )

    QRF: Optional[_QRF] = Field(
        default=None,
        title="QRF",
        description="Original style query filter",
    )

    PIDNTEORCOBRNTETQ1TQ2CTDOBXNTECTI_SUPPGRP: List[_ORF_R04_PIDNTEORCOBRNTETQ1TQ2CTDOBXNTECTI_SUPPGRP] = Field(
        min_length=1,
        title="PIDNTEORCOBRNTETQ1TQ2CTDOBXNTECTI_SUPPGRP",
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

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="Continuation Pointer",
    )

    model_config = ConfigDict(populate_by_name=True)
