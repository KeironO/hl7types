"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: RSP_E03.QUERY_ACK_IPR
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
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
        QAK (Optional[QAK]): optional
        QPD (Optional[QPD]): optional
        IPR (Optional[List[IPR]]): optional
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

    IPR: Optional[List[_IPR]] = Field(
        default=None,
        title="IPR",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
