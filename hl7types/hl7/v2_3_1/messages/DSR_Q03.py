"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: DSR_Q03
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.DSC import DSC
from ..segments.DSP import DSP
from ..segments.ERR import ERR
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.QAK import QAK
from ..segments.QRD import QRD
from ..segments.QRF import QRF

_DSC = DSC
_DSP = DSP
_ERR = ERR
_MSA = MSA
_MSH = MSH
_QAK = QAK
_QRD = QRD
_QRF = QRF


class DSR_Q03(HL7Model):
    """DSR/ACK - Deferred response to a query.

    Attributes:
        MSH (MSH): MSH - message header segment, required
        MSA (Optional[MSA]): MSA - message acknowledgment segment, optional
        ERR (Optional[ERR]): ERR - error segment, optional
        QAK (Optional[QAK]): Query Acknowledgement, optional
        QRD (QRD): QRD - original-style query definition segment, required
        QRF (Optional[QRF]): QRF - original style query filter segment, optional
        DSP (List[DSP]): DSP - display data segment, required
        DSC (Optional[DSC]): DSC - Continuation pointer segment, optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="MSH - message header segment",
    )

    MSA: Optional[_MSA] = Field(
        default=None,
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

    QRF: Optional[_QRF] = Field(
        default=None,
        title="QRF",
        description="QRF - original style query filter segment",
    )

    DSP: List[_DSP] = Field(
        min_length=1,
        title="DSP",
        description="DSP - display data segment",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="DSC - Continuation pointer segment",
    )

    model_config = ConfigDict(populate_by_name=True)
