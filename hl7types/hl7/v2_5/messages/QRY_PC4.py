"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: QRY_PC4
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH
from ..segments.QRD import QRD
from ..segments.QRF import QRF
from ..segments.SFT import SFT

_MSH = MSH
_QRD = QRD
_QRF = QRF
_SFT = SFT


class QRY_PC4(HL7Model):
    """QRY - PC/ problem query (S3.3.19).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        QRD (QRD): Original-Style Query Definition, required
        QRF (Optional[QRF]): Original style query filter, optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message Header",
    )

    SFT: Optional[List[_SFT]] = Field(
        default=None,
        title="SFT",
        description="Software Segment",
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
