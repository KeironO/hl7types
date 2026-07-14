"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: ADT_A42
Type: Message
"""
from __future__ import annotations

from .ADT_A39 import ADT_A39


class ADT_A42(ADT_A39):
    """ADT/ACK - Merge visit - visit number (S3.3.42).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        EVN (EVN): Event Type, required
        PATIENT (List[ADT_A39_PATIENT]): required
    """

    pass
