"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: ADT_A47
Type: Message
"""
from __future__ import annotations

from .ADT_A44 import ADT_A44


class ADT_A47(ADT_A44):
    """ADT/ACK - Change patient identifier list (S3.3.47).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        EVN (EVN): Event Type, required
        PATIENT (List[ADT_A44_PATIENT]): required
    """

    pass
