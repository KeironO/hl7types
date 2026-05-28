"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: ORF_R04
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.ORF_R04_QUERY_RESPONSE import ORF_R04_QUERY_RESPONSE
from ..segments.DSC import DSC
from ..segments.ERR import ERR
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.QAK import QAK
from ..segments.QRD import QRD
from ..segments.QRF import QRF
from ..segments.SFT import SFT

_DSC = DSC
_ERR = ERR
_MSA = MSA
_MSH = MSH
_ORF_R04_QUERY_RESPONSE = ORF_R04_QUERY_RESPONSE
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
        QUERY_RESPONSE (List[ORF_R04_QUERY_RESPONSE]): required
        ERR (Optional[List[ERR]]): optional
        QAK (Optional[QAK]): optional
        DSC (Optional[DSC]): optional
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    SFT: list[_SFT] | None = Field(
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

    QRF: _QRF | None = Field(
        default=None,
        title="QRF",
        description="Optional",
    )

    QUERY_RESPONSE: list[_ORF_R04_QUERY_RESPONSE] = Field(
        default=...,
        title="QUERY_RESPONSE",
        description="Required, repeating",
    )

    ERR: list[_ERR] | None = Field(
        default=None,
        title="ERR",
        description="Optional, repeating",
    )

    QAK: _QAK | None = Field(
        default=None,
        title="QAK",
        description="Optional",
    )

    DSC: _DSC | None = Field(
        default=None,
        title="DSC",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
