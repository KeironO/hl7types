"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: QBP_E22
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.QBP_E22_QUERY import QBP_E22_QUERY
from ..segments.MSH import MSH
from ..segments.SFT import SFT
from ..segments.UAC import UAC

_MSH = MSH
_QBP_E22_QUERY = QBP_E22_QUERY
_SFT = SFT
_UAC = UAC


class QBP_E22(BaseModel):
    """HL7 v2 QBP_E22 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[List[UAC]]): optional
        QUERY (QBP_E22_QUERY): required
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

    QUERY: _QBP_E22_QUERY = Field(
        default=...,
        title="QUERY",
        description="Required",
    )

    model_config = {"populate_by_name": True}
