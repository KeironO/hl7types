"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: QRY_R02
Type: Message
"""
from __future__ import annotations

from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH
from ..segments.QRD import QRD
from ..segments.QRF import QRF

_MSH = MSH
_QRD = QRD
_QRF = QRF


class QRY_R02(HL7Model):
    """QRY - Query for results of observation.

    Attributes:
        MSH (MSH): Message header segment, required
        QRD (QRD): Query definition segment, required
        QRF (QRF): Query filter segment, required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message header segment",
    )

    QRD: _QRD = Field(
        title="QRD",
        description="Query definition segment",
    )

    QRF: _QRF = Field(
        title="QRF",
        description="Query filter segment",
    )

    model_config = ConfigDict(populate_by_name=True)
