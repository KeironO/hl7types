"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: SLR_S28
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH
from ..segments.SFT import SFT
from ..segments.SLT import SLT
from ..segments.UAC import UAC

_MSH = MSH
_SFT = SFT
_SLT = SLT
_UAC = UAC


class SLR_S28(HL7Model):
    """HL7 v2 SLR_S28 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        SLT (List[SLT]): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Required",
    )

    SFT: Optional[List[_SFT]] = Field(
        default=None,
        title="SFT",
        description="Optional, repeating",
    )

    UAC: Optional[_UAC] = Field(
        default=None,
        title="UAC",
        description="Optional",
    )

    SLT: List[_SLT] = Field(
        min_length=1,
        title="SLT",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
