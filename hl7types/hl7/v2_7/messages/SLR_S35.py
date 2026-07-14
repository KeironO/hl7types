"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: SLR_S35
Type: Message
"""
from __future__ import annotations

from .SLR_S28 import SLR_S28


class SLR_S35(SLR_S28):
    """SLN/ACK - Notification of sterilization lot deletion (S17.6.3).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        SLT (List[SLT]): Sterilization Lot, required
    """

    pass
