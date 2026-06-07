"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: VXQ_V01
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


class VXQ_V01(HL7Model):
    """HL7 v2 VXQ_V01 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        QRD (QRD): required
        QRF (Optional[QRF]): optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Required",
    )

    SFT: Optional[List[_SFT]] = Field(
        default=None,
        title="SFT",
        description="Optional, repeating",
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
