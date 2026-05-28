"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: QRY_A19
Type: Message
"""
from _future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field

from ..segments.MSH import MSH
from ..segments.QRD import QRD

_MSH = MSH
_QRD = QRD


class QRY_A19(BaseModel):
    """HL7 v2 QRY_A19 message.

    Attributes:
        MSH (MSH): required
        QRD (QRD): required
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

    model_config = {"populate_by_name": True}
