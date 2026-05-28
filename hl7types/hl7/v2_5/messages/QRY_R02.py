"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: QRY_R02
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.MSH import MSH
from ..segments.QRD import QRD
from ..segments.QRF import QRF
from ..segments.SFT import SFT

_MSH = MSH
_QRD = QRD
_QRF = QRF
_SFT = SFT


class QRY_R02(BaseModel):
    """HL7 v2 QRY_R02 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        QRD (QRD): required
        QRF (QRF): required
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

    QRF: _QRF = Field(
        default=...,
        title="QRF",
        description="Required",
    )

    model_config = {"populate_by_name": True}
