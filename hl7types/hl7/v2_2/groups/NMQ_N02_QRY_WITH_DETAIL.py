"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: NMQ_N02.QRY_WITH_DETAIL
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


class NMQ_N02_QRY_WITH_DETAIL(HL7Model):
    """HL7 v2 NMQ_N02.QRY_WITH_DETAIL group.

    Attributes:
        QRD (QRD): QUERY DEFINITION, required
        QRF (Optional[QRF]): QUERY FILTER, optional
    """

    QRD: _QRD = Field(
        title="QRD",
        description="QUERY DEFINITION",
    )

    QRF: Optional[_QRF] = Field(
        default=None,
        title="QRF",
        description="QUERY FILTER",
    )

    model_config = {"populate_by_name": True}
