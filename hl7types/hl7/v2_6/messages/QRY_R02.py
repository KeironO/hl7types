"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: QRY_R02
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.MSH import MSH
from ..segments.QRD import QRD
from ..segments.QRF import QRF
from ..segments.SFT import SFT
from ..segments.UAC import UAC

_MSH = MSH
_QRD = QRD
_QRF = QRF
_SFT = SFT
_UAC = UAC


class QRY_R02(BaseModel):
    """HL7 v2 QRY_R02 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        QRD (QRD): required
        QRF (QRF): required
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

    UAC: Optional[_UAC] = Field(
        default=None,
        title="UAC",
        description="Optional",
    )

    QRD: _QRD = Field(
        default=...,
        title="QRD",
        description="Required",
    )

    QRF: _QRF = Field(
        default=...,
        title="QRF",
        description="Required",
    )

    model_config = {"populate_by_name": True}
