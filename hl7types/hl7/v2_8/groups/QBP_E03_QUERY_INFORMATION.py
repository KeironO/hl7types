"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: QBP_E03.QUERY_INFORMATION
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.QPD import QPD
from ..segments.RCP import RCP

_QPD = QPD
_RCP = RCP


class QBP_E03_QUERY_INFORMATION(HL7Model):
    """HL7 v2 QBP_E03.QUERY_INFORMATION group.

    Attributes:
        QPD (Optional[QPD]): optional
        RCP (Optional[RCP]): optional
    """

    QPD: Optional[_QPD] = Field(
        default=None,
        title="QPD",
        description="Optional",
    )

    RCP: Optional[_RCP] = Field(
        default=None,
        title="RCP",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
