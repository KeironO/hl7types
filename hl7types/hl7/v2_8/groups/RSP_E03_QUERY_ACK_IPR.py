"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: RSP_E03.QUERY_ACK_IPR
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.IPR import IPR
from ..segments.QAK import QAK
from ..segments.QPD import QPD

_IPR = IPR
_QAK = QAK
_QPD = QPD


class RSP_E03_QUERY_ACK_IPR(HL7Model):
    """HL7 v2 RSP_E03.QUERY_ACK_IPR group.

    Attributes:
        QAK (Optional[QAK]): Query Acknowledgment, optional
        QPD (Optional[QPD]): Query Parameter Definition, optional
        IPR (Optional[List[IPR]]): Invoice Processing Results, optional
    """

    QAK: Optional[_QAK] = Field(
        default=None,
        title="QAK",
        description="Query Acknowledgment",
    )

    QPD: Optional[_QPD] = Field(
        default=None,
        title="QPD",
        description="Query Parameter Definition",
    )

    IPR: Optional[List[_IPR]] = Field(
        default=None,
        title="IPR",
        description="Invoice Processing Results",
    )

    model_config = ConfigDict(populate_by_name=True)
