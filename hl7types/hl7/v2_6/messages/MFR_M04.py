"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: MFR_M04
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.MFR_M04_MF_QUERY import MFR_M04_MF_QUERY
from ..segments.DSC import DSC
from ..segments.ERR import ERR
from ..segments.MFI import MFI
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.QAK import QAK
from ..segments.QRD import QRD
from ..segments.QRF import QRF
from ..segments.SFT import SFT
from ..segments.UAC import UAC

_DSC = DSC
_ERR = ERR
_MFI = MFI
_MFR_M04_MF_QUERY = MFR_M04_MF_QUERY
_MSA = MSA
_MSH = MSH
_QAK = QAK
_QRD = QRD
_QRF = QRF
_SFT = SFT
_UAC = UAC


class MFR_M04(BaseModel):
    """HL7 v2 MFR_M04 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        MSA (MSA): required
        ERR (Optional[List[ERR]]): optional
        QAK (Optional[QAK]): optional
        QRD (QRD): required
        QRF (Optional[QRF]): optional
        MFI (MFI): required
        MF_QUERY (List[MFR_M04_MF_QUERY]): required
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

    UAC: _UAC | None = Field(
        default=None,
        title="UAC",
        description="Optional",
    )

    MSA: _MSA = Field(
        default=...,
        title="MSA",
        description="Required",
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

    MF_QUERY: list[_MFR_M04_MF_QUERY] = Field(
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
