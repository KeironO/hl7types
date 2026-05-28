"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: SDR_S31
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.SDR_S31_ANTI_MICROBIAL_DEVICE_DATA import SDR_S31_ANTI_MICROBIAL_DEVICE_DATA
from ..segments.MSH import MSH
from ..segments.SFT import SFT
from ..segments.UAC import UAC

_MSH = MSH
_SDR_S31_ANTI_MICROBIAL_DEVICE_DATA = SDR_S31_ANTI_MICROBIAL_DEVICE_DATA
_SFT = SFT
_UAC = UAC


class SDR_S31(BaseModel):
    """HL7 v2 SDR_S31 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        ANTI_MICROBIAL_DEVICE_DATA (SDR_S31_ANTI_MICROBIAL_DEVICE_DATA): required
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

    ANTI_MICROBIAL_DEVICE_DATA: _SDR_S31_ANTI_MICROBIAL_DEVICE_DATA = Field(
        default=...,
        title="ANTI_MICROBIAL_DEVICE_DATA",
        description="Required",
    )

    model_config = {"populate_by_name": True}
