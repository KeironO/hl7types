"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
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
    """QRY - Query for results of observation (S12).

    Attributes:
        MSH (MSH): Message Header, required
        QRD (QRD): Original-Style Query Definition, required
        QRF (QRF): Original Style Query Filter, required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message Header",
    )

    QRD: _QRD = Field(
        title="QRD",
        description="Original-Style Query Definition",
    )

    QRF: _QRF = Field(
        title="QRF",
        description="Original Style Query Filter",
    )

    model_config = ConfigDict(populate_by_name=True)
