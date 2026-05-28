"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: MFR_M01
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.MFR_M01_MF_QUERY import MFR_M01_MF_QUERY
from ..segments.DSC import DSC
from ..segments.ERR import ERR
from ..segments.MFI import MFI
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.QAK import QAK
from ..segments.QRD import QRD
from ..segments.QRF import QRF

_DSC = DSC
_ERR = ERR
_MFI = MFI
_MFR_M01_MF_QUERY = MFR_M01_MF_QUERY
_MSA = MSA
_MSH = MSH
_QAK = QAK
_QRD = QRD
_QRF = QRF


class MFR_M01(BaseModel):
    """HL7 v2 MFR_M01 message.

    Attributes:
        MSH (MSH): required
        MSA (MSA): required
        ERR (Optional[ERR]): optional
        QAK (Optional[QAK]): optional
        QRD (QRD): required
        QRF (Optional[QRF]): optional
        MFI (MFI): required
        MF_QUERY (List[MFR_M01_MF_QUERY]): required
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

    ERR: _ERR | None = Field(
        default=None,
        title="ERR",
        description="Optional",
    )

    QAK: _QAK | None = Field(
        default=None,
        title="QAK",
        description="Optional",
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

    MFI: _MFI = Field(
        default=...,
        title="MFI",
        description="Required",
    )

    MF_QUERY: list[_MFR_M01_MF_QUERY] = Field(
        default=...,
        title="MF_QUERY",
        description="Required, repeating",
    )

    DSC: _DSC | None = Field(
        default=None,
        title="DSC",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
