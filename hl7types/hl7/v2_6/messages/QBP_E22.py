"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: QBP_E22
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.QBP_E22_QUERY import QBP_E22_QUERY

_MSH = MSH
_QBP_E22_QUERY = QBP_E22_QUERY
_SFT = SFT
_UAC = UAC


class QBP_E22(HL7Model):
    """Authorization Request Status (S15.3.7).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[List[UAC]]): User Authentication Credential Segment, optional
        QUERY (QBP_E22_QUERY): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message Header",
    )

    SFT: Optional[List[_SFT]] = Field(
        default=None,
        title="SFT",
        description="Software Segment",
    )

    UAC: Optional[List[_UAC]] = Field(
        default=None,
        title="UAC",
        description="User Authentication Credential Segment",
    )

    QUERY: _QBP_E22_QUERY = Field(
        title="QUERY",
    )

    model_config = ConfigDict(populate_by_name=True)
