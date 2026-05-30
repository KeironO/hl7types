"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: OSQ_Q06
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


class OSQ_Q06(HL7Model):
    """HL7 v2 OSQ_Q06 message.

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

    QRF: Optional[_QRF] = Field(
        default=None,
        title="QRF",
        description="Optional",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
