"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
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

from ..groups.ORF_R04_QUERY_RESPONSE import ORF_R04_QUERY_RESPONSE

_DSC = DSC
_ERR = ERR
_MSA = MSA
_MSH = MSH
_ORF_R04_QUERY_RESPONSE = ORF_R04_QUERY_RESPONSE
_QAK = QAK
_QRD = QRD
_QRF = QRF


class ORF_R04(HL7Model):
    """ORF - Response to query; transmission of requested observation.

    Attributes:
        MSH (MSH): MSH - message header segment, required
        MSA (MSA): MSA - message acknowledgment segment, required
        QRD (QRD): QRD - original-style query definition segment, required
        QRF (Optional[QRF]): QRF - original style query filter segment, optional
        QUERY_RESPONSE (List[ORF_R04_QUERY_RESPONSE]): required
        ERR (Optional[ERR]): ERR - error segment, optional
        QAK (Optional[QAK]): Query Acknowledgement, optional
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

    QRD: _QRD = Field(
        title="QRD",
        description="QRD - original-style query definition segment",
    )

    QRF: Optional[_QRF] = Field(
        default=None,
        title="QRF",
        description="QRF - original style query filter segment",
    )

    QUERY_RESPONSE: List[_ORF_R04_QUERY_RESPONSE] = Field(
        min_length=1,
        title="QUERY_RESPONSE",
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

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="DSC - Continuation pointer segment",
    )

    model_config = ConfigDict(populate_by_name=True)
