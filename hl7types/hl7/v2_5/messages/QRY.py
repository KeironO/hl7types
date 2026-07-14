"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: QRY
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


class QRY(HL7Model):
    """HL7 v2 QRY message.

    Attributes:
        MSH (MSH): Message Header, required
        QRD (QRD): Original-Style Query Definition, required
        QRF (Optional[QRF]): Original style query filter, optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message Header",
    )

    QRD: _QRD = Field(
        title="QRD",
        description="Original-Style Query Definition",
    )

    QRF: Optional[_QRF] = Field(
        default=None,
        title="QRF",
        description="Original style query filter",
    )

    model_config = {"populate_by_name": True}
