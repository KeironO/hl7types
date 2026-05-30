"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
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

from ..groups.SDR_S32_ANTIMICROBIAL_DEVICE_CYCLE_DATA import SDR_S32_ANTIMICROBIAL_DEVICE_CYCLE_DATA

_MSH = MSH
_SDR_S32_ANTIMICROBIAL_DEVICE_CYCLE_DATA = SDR_S32_ANTIMICROBIAL_DEVICE_CYCLE_DATA
_SFT = SFT
_UAC = UAC


class SDR_S32(HL7Model):
    """HL7 v2 SDR_S32 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        ANTIMICROBIAL_DEVICE_CYCLE_DATA (SDR_S32_ANTIMICROBIAL_DEVICE_CYCLE_DATA): required
    """

    MSH: _MSH = Field(
        default=...,
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

    ANTIMICROBIAL_DEVICE_CYCLE_DATA: _SDR_S32_ANTIMICROBIAL_DEVICE_CYCLE_DATA = Field(
        default=...,
        title="ANTIMICROBIAL_DEVICE_CYCLE_DATA",
        description="Required",
    )

    model_config = {"populate_by_name": True}
