"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: DOC_T12
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

from ..groups.DOC_T12_RESULT import DOC_T12_RESULT

_DOC_T12_RESULT = DOC_T12_RESULT
_DSC = DSC
_ERR = ERR
_MSA = MSA
_MSH = MSH
_QAK = QAK
_QRD = QRD


class DOC_T12(HL7Model):
    """QRY/DOC - Document query.

    Attributes:
        MSH (MSH): MSH - message header segment, required
        MSA (MSA): MSA - message acknowledgment segment, required
        ERR (Optional[ERR]): ERR - error segment, optional
        QAK (Optional[QAK]): Query Acknowledgement, optional
        QRD (QRD): QRD - original-style query definition segment, required
        RESULT (List[DOC_T12_RESULT]): required
        DSC (Optional[DSC]): DSC - Continuation pointer segment, optional
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

    RESULT: List[_DOC_T12_RESULT] = Field(
        min_length=1,
        title="RESULT",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="DSC - Continuation pointer segment",
    )

    model_config = ConfigDict(populate_by_name=True)
