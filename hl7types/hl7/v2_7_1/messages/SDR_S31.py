"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: SDR_S31
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.SDR_S31_ANTI_MICROBIAL_DEVICE_DATA import SDR_S31_ANTI_MICROBIAL_DEVICE_DATA

_MSH = MSH
_SDR_S31_ANTI_MICROBIAL_DEVICE_DATA = SDR_S31_ANTI_MICROBIAL_DEVICE_DATA
_SFT = SFT
_UAC = UAC


class SDR_S31(HL7Model):
    """SDR/SDS - Request anti-microbial device data (S17.5.4).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        ANTI_MICROBIAL_DEVICE_DATA (SDR_S31_ANTI_MICROBIAL_DEVICE_DATA): required
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

    ANTI_MICROBIAL_DEVICE_DATA: _SDR_S31_ANTI_MICROBIAL_DEVICE_DATA = Field(
        title="ANTI_MICROBIAL_DEVICE_DATA",
    )

    model_config = ConfigDict(populate_by_name=True)
