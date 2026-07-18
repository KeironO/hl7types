"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: MFR_M01
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.DSC import DSC
from ..segments.ERR import ERR
from ..segments.MFI import MFI
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.QAK import QAK
from ..segments.QRD import QRD
from ..segments.QRF import QRF

from ..groups.MFR_M01_MF_QUERY import MFR_M01_MF_QUERY

_DSC = DSC
_ERR = ERR
_MFI = MFI
_MFR_M01_MF_QUERY = MFR_M01_MF_QUERY
_MSA = MSA
_MSH = MSH
_QAK = QAK
_QRD = QRD
_QRF = QRF


class MFR_M01(HL7Model):
    """MFN/MFK - Master file not otherwise specified (for backward compatibility only).

    Attributes:
        MSH (MSH): MSH - message header segment, required
        MSA (MSA): MSA - message acknowledgment segment, required
        ERR (Optional[ERR]): ERR - error segment, optional
        QAK (Optional[QAK]): Query Acknowledgement, optional
        QRD (QRD): QRD - original-style query definition segment, required
        QRF (Optional[QRF]): QRF - original style query filter segment, optional
        MFI (MFI): MFI - master file identification segment, required
        MF_QUERY (List[MFR_M01_MF_QUERY]): required
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

    QRF: Optional[_QRF] = Field(
        default=None,
        title="QRF",
        description="QRF - original style query filter segment",
    )

    MFI: _MFI = Field(
        title="MFI",
        description="MFI - master file identification segment",
    )

    MF_QUERY: List[_MFR_M01_MF_QUERY] = Field(
        min_length=1,
        title="MF_QUERY",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="DSC - Continuation pointer segment",
    )

    model_config = ConfigDict(populate_by_name=True)
