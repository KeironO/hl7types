"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: SLR_S28
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.MSH import MSH
from ..segments.SFT import SFT
from ..segments.SLT import SLT
from ..segments.UAC import UAC

_MSH = MSH
_SFT = SFT
_SLT = SLT
_UAC = UAC


class SLR_S28(BaseModel):
    """HL7 v2 SLR_S28 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        SLT (List[SLT]): required
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

    UAC: _UAC | None = Field(
        default=None,
        title="UAC",
        description="Optional",
    )

    SLT: list[_SLT] = Field(
        default=...,
        title="SLT",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
