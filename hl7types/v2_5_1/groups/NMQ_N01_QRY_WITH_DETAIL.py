"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: NMQ_N01.QRY_WITH_DETAIL
Type: Group
"""
from _future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field

from ..segments.QRD import QRD
from ..segments.QRF import QRF

_QRD = QRD
_QRF = QRF


class NMQ_N01_QRY_WITH_DETAIL(BaseModel):
    """HL7 v2 NMQ_N01.QRY_WITH_DETAIL group.

    Attributes:
        QRD (QRD): required
        QRF (Optional[QRF]): optional
    """

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

    model_config = {"populate_by_name": True}
