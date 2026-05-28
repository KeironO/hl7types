"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: ORF_R04
Type: Message
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

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


class ORF_R04(BaseModel):
    """HL7 v2 ORF_R04 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        MSA (MSA): required
        QRD (QRD): required
        QRF (Optional[QRF]): optional
        PIDNTEORCOBRNTETQ1TQ2CTDOBXNTECTI_SUPPGRP (List[ORF_R04_PIDNTEORCOBRNTETQ1TQ2CTDOBXNTECTI_SUPPGRP]): required
        ERR (Optional[List[ERR]]): optional
        QAK (Optional[QAK]): optional
        DSC (Optional[DSC]): optional
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    SFT: Optional[List[_SFT]] = Field(
        default=None,
        title="SFT",
        description="Optional, repeating",
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

    QRF: Optional[_QRF] = Field(
        default=None,
        title="QRF",
        description="Optional",
    )

    PIDNTEORCOBRNTETQ1TQ2CTDOBXNTECTI_SUPPGRP: List[_ORF_R04_PIDNTEORCOBRNTETQ1TQ2CTDOBXNTECTI_SUPPGRP] = Field(
        default=...,
        title="PIDNTEORCOBRNTETQ1TQ2CTDOBXNTECTI_SUPPGRP",
        description="Required, repeating",
    )

    ERR: Optional[List[_ERR]] = Field(
        default=None,
        title="ERR",
        description="Optional, repeating",
    )

    QAK: Optional[_QAK] = Field(
        default=None,
        title="QAK",
        description="Optional",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
