"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: MFR_M07
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.DSC import DSC
from ..segments.ERR import ERR
from ..segments.MFI import MFI
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.QAK import QAK
from ..segments.QRD import QRD
from ..segments.QRF import QRF
from ..segments.SFT import SFT

from ..groups.MFR_M07_MF_QUERY import MFR_M07_MF_QUERY

_DSC = DSC
_ERR = ERR
_MFI = MFI
_MFR_M07_MF_QUERY = MFR_M07_MF_QUERY
_MSA = MSA
_MSH = MSH
_QAK = QAK
_QRD = QRD
_QRF = QRF
_SFT = SFT


class MFR_M07(HL7Model):
    """HL7 v2 MFR_M07 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        MSA (MSA): required
        ERR (Optional[List[ERR]]): optional
        QAK (Optional[QAK]): optional
        QRD (QRD): required
        QRF (Optional[QRF]): optional
        MFI (MFI): required
        MF_QUERY (List[MFR_M07_MF_QUERY]): required
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

    MFI: _MFI = Field(
        default=...,
        title="MFI",
        description="Required",
    )

    MF_QUERY: List[_MFR_M07_MF_QUERY] = Field(
        default=...,
        title="MF_QUERY",
        description="Required, repeating",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
