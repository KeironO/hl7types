"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: QRY_A19
Type: Message
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH
from ..segments.QRD import QRD
from ..segments.QRF import QRF

_MSH = MSH
_QRD = QRD
_QRF = QRF


class QRY_A19(HL7Model):
    """HL7 v2 QRY_A19 message.

    Attributes:
        MSH (MSH): required
        QRD (QRD): required
        QRF (Optional[QRF]): optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Required",
    )

    QRD: _QRD = Field(
        title="QRD",
        description="Required",
    )

    QRF: Optional[_QRF] = Field(
        default=None,
        title="QRF",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
