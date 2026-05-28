"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: SQM_S25
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.SQM_S25_REQUEST import SQM_S25_REQUEST
from ..segments.DSC import DSC
from ..segments.MSH import MSH
from ..segments.QRD import QRD
from ..segments.QRF import QRF

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

    QRF: _QRF | None = Field(
        default=None,
        title="QRF",
        description="Optional",
    )

    REQUEST: _SQM_S25_REQUEST | None = Field(
        default=None,
        title="REQUEST",
        description="Optional",
    )

    DSC: _DSC | None = Field(
        default=None,
        title="DSC",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
