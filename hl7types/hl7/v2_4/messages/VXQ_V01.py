"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
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
    """VXQ - Query for vaccination record (S4).

    Attributes:
        MSH (MSH): Message Header, required
        QRD (QRD): Original-Style Query Definition, required
        QRF (Optional[QRF]): Original Style Query Filter, optional
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
        description="Original Style Query Filter",
    )

    model_config = {"populate_by_name": True}
