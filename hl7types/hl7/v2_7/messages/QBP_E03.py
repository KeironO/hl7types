"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: QBP_E03
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.QBP_E03_QUERY_INFORMATION import QBP_E03_QUERY_INFORMATION

_MSH = MSH
_QBP_E03_QUERY_INFORMATION = QBP_E03_QUERY_INFORMATION
_SFT = SFT
_UAC = UAC


class QBP_E03(HL7Model):
    """HealthCare Services Invoice Status (S15.3.7).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[List[UAC]]): User Authentication Credential Segment, optional
        QUERY_INFORMATION (QBP_E03_QUERY_INFORMATION): required
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

    QUERY_INFORMATION: _QBP_E03_QUERY_INFORMATION = Field(
        title="QUERY_INFORMATION",
    )

    model_config = {"populate_by_name": True}
