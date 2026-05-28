"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: QRY
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.MSH import MSH
from ..segments.QRD import QRD
from ..segments.QRF import QRF

_MSH = MSH
_QRD = QRD
_QRF = QRF


class QRY(BaseModel):
    """HL7 v2 QRY message.

    Attributes:
        MSH (MSH): required
        QRD (QRD): required
        QRF (Optional[QRF]): optional
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
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

    model_config = {"populate_by_name": True}
