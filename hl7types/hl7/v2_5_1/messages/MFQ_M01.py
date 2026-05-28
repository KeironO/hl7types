"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: MFQ_M01
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.DSC import DSC
from ..segments.MSH import MSH
from ..segments.QRD import QRD
from ..segments.QRF import QRF
from ..segments.SFT import SFT

_DSC = DSC
_MSH = MSH
_QRD = QRD
_QRF = QRF
_SFT = SFT


class MFQ_M01(BaseModel):
    """HL7 v2 MFQ_M01 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        QRD (QRD): required
        QRF (Optional[QRF]): optional
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

    DSC: _DSC | None = Field(
        default=None,
        title="DSC",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
