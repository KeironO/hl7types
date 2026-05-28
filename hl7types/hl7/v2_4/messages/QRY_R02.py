"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: QRY_R02
Type: Message
"""
from __future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field

from ..segments.MSH import MSH
from ..segments.QRD import QRD
from ..segments.QRF import QRF

_MSH = MSH
_QRD = QRD
_QRF = QRF


class QRY_R02(BaseModel):
    """HL7 v2 QRY_R02 message.

    Attributes:
        MSH (MSH): required
        QRD (QRD): required
        QRF (QRF): required
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

    QRF: _QRF = Field(
        default=...,
        title="QRF",
        description="Required",
    )

    model_config = {"populate_by_name": True}
