"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: QRY_R02
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


class QRY_R02(HL7Model):
    """QRY - Query for results of observation (S12.3.11).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        QRD (QRD): Original-Style Query Definition, required
        QRF (QRF): Original style query filter, required
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
        description="Original-Style Query Definition",
    )

    QRF: _QRF = Field(
        title="QRF",
        description="Original style query filter",
    )

    model_config = {"populate_by_name": True}
