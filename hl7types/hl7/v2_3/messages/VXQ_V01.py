"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: VXQ_V01
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


class VXQ_V01(HL7Model):
    """VXQ - Query for vaccination record.

    Attributes:
        MSH (MSH): Message header segment, required
        QRD (QRD): Query definition segment, required
        QRF (Optional[QRF]): Query filter segment, optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message header segment",
    )

    QRD: _QRD = Field(
        title="QRD",
        description="Query definition segment",
    )

    QRF: Optional[_QRF] = Field(
        default=None,
        title="QRF",
        description="Query filter segment",
    )

    model_config = {"populate_by_name": True}
