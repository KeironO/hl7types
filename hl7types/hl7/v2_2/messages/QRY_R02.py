"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: QRY_R02
Type: Message
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.DSC import DSC
from ..segments.MSH import MSH
from ..segments.QRD import QRD
from ..segments.QRF import QRF

_DSC = DSC
_MSH = MSH
_QRD = QRD
_QRF = QRF


class QRY_R02(HL7Model):
    """HL7 v2 QRY_R02 message.

    Attributes:
        MSH (MSH): required
        QRD (QRD): required
        QRF (QRF): required
        DSC (Optional[DSC]): optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Required",
    )

    QRD: _QRD = Field(
        title="QRD",
        description="Required",
    )

    QRF: _QRF = Field(
        title="QRF",
        description="Required",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
