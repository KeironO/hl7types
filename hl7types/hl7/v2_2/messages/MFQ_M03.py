"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: MFQ_M03
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.DSC import DSC
from ..segments.MSH import MSH
from ..segments.QRD import QRD
from ..segments.QRF import QRF

_DSC = DSC
_MSH = MSH
_QRD = QRD
_QRF = QRF


class MFQ_M03(BaseModel):
    """HL7 v2 MFQ_M03 message.

    Attributes:
        MSH (MSH): required
        QRD (QRD): required
        QRF (Optional[QRF]): optional
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

    DSC: _DSC | None = Field(
        default=None,
        title="DSC",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
