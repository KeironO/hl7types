"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: SQM_S25
Type: Message
"""
from _future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field

from ..segments.DSC import DSC
from ..segments.MSH import MSH
from ..segments.QRD import QRD
from ..segments.QRF import QRF

from ..groups.SQM_S25_REQUEST import SQM_S25_REQUEST

_DSC = DSC
_MSH = MSH
_QRD = QRD
_QRF = QRF
_SQM_S25_REQUEST = SQM_S25_REQUEST


class SQM_S25(BaseModel):
    """HL7 v2 SQM_S25 message.

    Attributes:
        MSH (MSH): required
        QRD (QRD): required
        QRF (Optional[QRF]): optional
        REQUEST (Optional[SQM_S25_REQUEST]): optional
        DSC (Optional[DSC]): optional
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

    QRF: Optional[_QRF] = Field(
        default=None,
        title="QRF",
        description="Optional",
    )

    REQUEST: Optional[_SQM_S25_REQUEST] = Field(
        default=None,
        title="REQUEST",
        description="Optional",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
