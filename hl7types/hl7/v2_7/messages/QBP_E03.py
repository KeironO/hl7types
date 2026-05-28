"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: QBP_E03
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.QBP_E03_QUERY_INFORMATION import QBP_E03_QUERY_INFORMATION
from ..segments.MSH import MSH
from ..segments.SFT import SFT
from ..segments.UAC import UAC

_MSH = MSH
_QBP_E03_QUERY_INFORMATION = QBP_E03_QUERY_INFORMATION
_SFT = SFT
_UAC = UAC


class QBP_E03(BaseModel):
    """HL7 v2 QBP_E03 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[List[UAC]]): optional
        QUERY_INFORMATION (QBP_E03_QUERY_INFORMATION): required
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    SFT: list[_SFT] | None = Field(
        default=None,
        title="SFT",
        description="Optional, repeating",
    )

    UAC: list[_UAC] | None = Field(
        default=None,
        title="UAC",
        description="Optional, repeating",
    )

    QUERY_INFORMATION: _QBP_E03_QUERY_INFORMATION = Field(
        default=...,
        title="QUERY_INFORMATION",
        description="Required",
    )

    model_config = {"populate_by_name": True}
