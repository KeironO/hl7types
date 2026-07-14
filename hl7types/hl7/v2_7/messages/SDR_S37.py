"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: SDR_S37
Type: Message
"""
from __future__ import annotations

from .SDR_S32 import SDR_S32


class SDR_S37(SDR_S32):
    """SCN/ACK - Notification of anti-microbial device cycle data (S17.6.5).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        ANTI_MICROBIAL_DEVICE_CYCLE_DATA (SDR_S32_ANTI_MICROBIAL_DEVICE_CYCLE_DATA): required
    """

    pass
