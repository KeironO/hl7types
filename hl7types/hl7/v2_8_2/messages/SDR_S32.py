"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: SDR_S32
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.SDR_S32_ANTI_MICROBIAL_DEVICE_CYCLE_DATA import SDR_S32_ANTI_MICROBIAL_DEVICE_CYCLE_DATA

_MSH = MSH
_SDR_S32_ANTI_MICROBIAL_DEVICE_CYCLE_DATA = SDR_S32_ANTI_MICROBIAL_DEVICE_CYCLE_DATA
_SFT = SFT
_UAC = UAC


class SDR_S32(HL7Model):
    """SMD/SMS - Request anti-microbial device cycle data (S17.5.4).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        ANTI_MICROBIAL_DEVICE_CYCLE_DATA (SDR_S32_ANTI_MICROBIAL_DEVICE_CYCLE_DATA): required
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

    ANTI_MICROBIAL_DEVICE_CYCLE_DATA: _SDR_S32_ANTI_MICROBIAL_DEVICE_CYCLE_DATA = Field(
        title="ANTI_MICROBIAL_DEVICE_CYCLE_DATA",
    )

    model_config = {"populate_by_name": True}
