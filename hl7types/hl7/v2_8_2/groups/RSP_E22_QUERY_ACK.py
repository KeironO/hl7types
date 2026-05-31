"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: RSP_E22.QUERY_ACK
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.QAK import QAK
from ..segments.QPD import QPD

from .RSP_E22_AUTHORIZATION_INFO import RSP_E22_AUTHORIZATION_INFO

_QAK = QAK
_QPD = QPD
_RSP_E22_AUTHORIZATION_INFO = RSP_E22_AUTHORIZATION_INFO


class RSP_E22_QUERY_ACK(HL7Model):
    """HL7 v2 RSP_E22.QUERY_ACK group.

    Attributes:
        QAK (Optional[QAK]): optional
        QPD (Optional[QPD]): optional
        AUTHORIZATION_INFO (Optional[RSP_E22_AUTHORIZATION_INFO]): optional
    """

    QAK: Optional[_QAK] = Field(
        default=None,
        title="QAK",
        description="Optional",
    )

    QPD: Optional[_QPD] = Field(
        default=None,
        title="QPD",
        description="Optional",
    )

    AUTHORIZATION_INFO: Optional[_RSP_E22_AUTHORIZATION_INFO] = Field(
        default=None,
        title="AUTHORIZATION_INFO",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
