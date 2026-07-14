"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: SDR_S36
Type: Message
"""
from __future__ import annotations

from .SDR_S31 import SDR_S31


class SDR_S36(SDR_S31):
    """SDN/ACK - Notification of anti-microbial device data (S17.6.4).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        ANTI_MICROBIAL_DEVICE_DATA (SDR_S31_ANTI_MICROBIAL_DEVICE_DATA): required
    """

    pass
