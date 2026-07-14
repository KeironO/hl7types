"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: ADR_A19
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.DSC import DSC
from ..segments.ERR import ERR
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.QAK import QAK
from ..segments.QRD import QRD
from ..segments.QRF import QRF

from ..groups.ADR_A19_QUERY_RESPONSE import ADR_A19_QUERY_RESPONSE

_ADR_A19_QUERY_RESPONSE = ADR_A19_QUERY_RESPONSE
_DSC = DSC
_ERR = ERR
_MSA = MSA
_MSH = MSH
_QAK = QAK
_QRD = QRD
_QRF = QRF


class ADR_A19(HL7Model):
    """QRY/ADR -  Patient query (S3).

    Attributes:
        MSH (MSH): Message Header, required
        MSA (MSA): Message Acknowledgment, required
        ERR (Optional[ERR]): Error, optional
        QAK (Optional[QAK]): Query Acknowledgment, optional
        QRD (QRD): Original-Style Query Definition, required
        QRF (Optional[QRF]): Original Style Query Filter, optional
        QUERY_RESPONSE (List[ADR_A19_QUERY_RESPONSE]): required
        DSC (Optional[DSC]): Continuation Pointer, optional
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

    QRF: Optional[_QRF] = Field(
        default=None,
        title="QRF",
        description="Original Style Query Filter",
    )

    QUERY_RESPONSE: List[_ADR_A19_QUERY_RESPONSE] = Field(
        min_length=1,
        title="QUERY_RESPONSE",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="Continuation Pointer",
    )

    model_config = {"populate_by_name": True}
