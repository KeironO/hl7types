"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: QBP_E22.QUERY
Type: Group
"""
from __future__ import annotations

from typing import Optional
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.QPD import QPD
from ..segments.RCP import RCP

_QPD = QPD
_RCP = RCP


class QBP_E22_QUERY(HL7Model):
    """HL7 v2 QBP_E22.QUERY group.

    Attributes:
        QPD (Optional[QPD]): Query Parameter Definition, optional
        RCP (Optional[RCP]): Response Control Parameter, optional
    """

    QPD: Optional[_QPD] = Field(
        default=None,
        title="QPD",
        description="Query Parameter Definition",
    )

    RCP: Optional[_RCP] = Field(
        default=None,
        title="RCP",
        description="Response Control Parameter",
    )

    model_config = ConfigDict(populate_by_name=True)
