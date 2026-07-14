"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: SLR_S30
Type: Message
"""
from __future__ import annotations

from .SLR_S28 import SLR_S28


class SLR_S30(SLR_S28):
    """STI/STS - Request item (S17.5.3).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        SLT (List[SLT]): Sterilization Lot, required
    """

    pass
