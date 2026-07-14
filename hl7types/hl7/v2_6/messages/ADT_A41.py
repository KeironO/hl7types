"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: ADT_A41
Type: Message
"""
from __future__ import annotations

from .ADT_A39 import ADT_A39


class ADT_A41(ADT_A39):
    """ADT/ACK - Merge account - patient account number (S3.3.41).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        EVN (EVN): Event Type, required
        PATIENT (List[ADT_A39_PATIENT]): required
    """

    pass
