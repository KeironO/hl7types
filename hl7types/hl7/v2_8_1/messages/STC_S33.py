"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: STC_S33
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
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
    """STC/ACK - Notification of sterilization configuration (S17.6.1).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        SCP (List[SCP]): Sterilizer Configuration (Anti-Microbial Devices), required
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

    UAC: Optional[_UAC] = Field(
        default=None,
        title="UAC",
        description="User Authentication Credential Segment",
    )

    SCP: List[_SCP] = Field(
        min_length=1,
        title="SCP",
        description="Sterilizer Configuration (Anti-Microbial Devices)",
    )

    model_config = ConfigDict(populate_by_name=True)
