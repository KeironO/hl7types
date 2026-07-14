"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: DOC_T12
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

from ..groups.DOC_T12_RESULT import DOC_T12_RESULT

_DOC_T12_RESULT = DOC_T12_RESULT
_DSC = DSC
_ERR = ERR
_MSA = MSA
_MSH = MSH
_QAK = QAK
_QRD = QRD


class DOC_T12(HL7Model):
    """QRY/DOC - Document query (S9).

    Attributes:
        MSH (MSH): Message Header, required
        MSA (MSA): Message Acknowledgment, required
        ERR (Optional[ERR]): Error, optional
        QAK (Optional[QAK]): Query Acknowledgment, optional
        QRD (QRD): Original-Style Query Definition, required
        RESULT (List[DOC_T12_RESULT]): required
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

    RESULT: List[_DOC_T12_RESULT] = Field(
        min_length=1,
        title="RESULT",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="Continuation Pointer",
    )

    model_config = {"populate_by_name": True}
