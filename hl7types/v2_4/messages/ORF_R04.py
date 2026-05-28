"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
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

from ..groups.ORF_R04_RESPONSE import ORF_R04_RESPONSE

_DSC = DSC
_ERR = ERR
_MSA = MSA
_MSH = MSH
_ORF_R04_RESPONSE = ORF_R04_RESPONSE
_QAK = QAK
_QRD = QRD
_QRF = QRF


class ORF_R04(BaseModel):
    """HL7 v2 ORF_R04 message.

    Attributes:
        MSH (MSH): required
        MSA (MSA): required
        QRD (QRD): required
        QRF (Optional[QRF]): optional
        RESPONSE (List[ORF_R04_RESPONSE]): required
        ERR (Optional[ERR]): optional
        QAK (Optional[QAK]): optional
        DSC (Optional[DSC]): optional
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

    RESPONSE: List[_ORF_R04_RESPONSE] = Field(
        default=...,
        title="RESPONSE",
        description="Required, repeating",
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

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
