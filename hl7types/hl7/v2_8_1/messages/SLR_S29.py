"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: SLR_S29
Type: Message
"""
from __future__ import annotations

from .SLR_S28 import SLR_S28


class SLR_S29(SLR_S28):
    """SLR/SLS - Request Sterilization lot deletion (S17.5.2).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        SLT (List[SLT]): Sterilization Lot, required
    """

    pass
