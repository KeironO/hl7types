"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: ADT_A49
Type: Message
"""
from __future__ import annotations

from .ADT_A43 import ADT_A43


class ADT_A49(ADT_A43):
    """ADT/ACK - Change patient account number (S3.3.49).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        EVN (EVN): Event Type, required
        PATIENT (List[ADT_A43_PATIENT]): required
    """

    pass
