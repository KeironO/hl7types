"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: RSP_E03.QUERY_ACK
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.QAK import QAK
from ..segments.QPD import QPD

from .RSP_E03_INVOICE_PROCESSING_RESULTS_INFO import RSP_E03_INVOICE_PROCESSING_RESULTS_INFO

_QAK = QAK
_QPD = QPD
_RSP_E03_INVOICE_PROCESSING_RESULTS_INFO = RSP_E03_INVOICE_PROCESSING_RESULTS_INFO


class RSP_E03_QUERY_ACK(HL7Model):
    """HL7 v2 RSP_E03.QUERY_ACK group.

    Attributes:
        QAK (Optional[QAK]): optional
        QPD (Optional[QPD]): optional
        INVOICE_PROCESSING_RESULTS_INFO (Optional[List[RSP_E03_INVOICE_PROCESSING_RESULTS_INFO]]): optional
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

    INVOICE_PROCESSING_RESULTS_INFO: Optional[List[_RSP_E03_INVOICE_PROCESSING_RESULTS_INFO]] = Field(
        default=None,
        title="INVOICE_PROCESSING_RESULTS_INFO",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
