"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: QBP_Z73
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.MSH import MSH
from ..segments.QPD import QPD
from ..segments.RCP import RCP
from ..segments.SFT import SFT

_MSH = MSH
_QPD = QPD
_RCP = RCP
_SFT = SFT


class QBP_Z73(BaseModel):
    """HL7 v2 QBP_Z73 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        QPD (QPD): required
        RCP (RCP): required
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

    QPD: _QPD = Field(
        default=...,
        title="QPD",
        description="Required",
    )

    RCP: _RCP = Field(
        default=...,
        title="RCP",
        description="Required",
    )

    model_config = {"populate_by_name": True}
