"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: NMQ_N01.QRY_WITH_DETAIL
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.QRD import QRD
from ..segments.QRF import QRF

_QRD = QRD
_QRF = QRF


class NMQ_N01_QRY_WITH_DETAIL(HL7Model):
    """HL7 v2 NMQ_N01.QRY_WITH_DETAIL group.

    Attributes:
        QRD (QRD): required
        QRF (Optional[QRF]): optional
    """

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
