"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
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
from ..segments.UAC import UAC

_MSH = MSH
_QRD = QRD
_QRF = QRF
_SFT = SFT
_UAC = UAC


class QRY_PC4(HL7Model):
    """QRY - PC/ problem query (S12.3.11).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        QRD (QRD): withdrawn, required
        QRF (Optional[QRF]): withdrawn, optional
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

    UAC: Optional[_UAC] = Field(
        default=None,
        title="UAC",
        description="User Authentication Credential Segment",
    )

    QRD: _QRD = Field(
        title="QRD",
        description="withdrawn",
    )

    QRF: Optional[_QRF] = Field(
        default=None,
        title="QRF",
        description="withdrawn",
    )

    model_config = {"populate_by_name": True}
