"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: SDR_S31
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.SDR_S31_ANTIMICROBIAL_DEVICE_DATA import SDR_S31_ANTIMICROBIAL_DEVICE_DATA

_MSH = MSH
_SDR_S31_ANTIMICROBIAL_DEVICE_DATA = SDR_S31_ANTIMICROBIAL_DEVICE_DATA
_SFT = SFT
_UAC = UAC


class SDR_S31(HL7Model):
    """HL7 v2 SDR_S31 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        ANTIMICROBIAL_DEVICE_DATA (SDR_S31_ANTIMICROBIAL_DEVICE_DATA): required
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

    ANTIMICROBIAL_DEVICE_DATA: _SDR_S31_ANTIMICROBIAL_DEVICE_DATA = Field(
        title="ANTIMICROBIAL_DEVICE_DATA",
        description="Required",
    )

    model_config = {"populate_by_name": True}
