"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: STC_S33
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH
from ..segments.SCP import SCP
from ..segments.SFT import SFT
from ..segments.UAC import UAC

_MSH = MSH
_SCP = SCP
_SFT = SFT
_UAC = UAC


class STC_S33(HL7Model):
    """HL7 v2 STC_S33 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        SCP (List[SCP]): required
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

    SCP: List[_SCP] = Field(
        min_length=1,
        title="SCP",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
