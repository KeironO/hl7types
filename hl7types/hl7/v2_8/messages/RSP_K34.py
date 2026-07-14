"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: RSP_K34
Type: Message
"""
from __future__ import annotations

from .RSP_O34 import RSP_O34


class RSP_K34(RSP_O34):
    """Segment Pattern Response Message (S4.16.9).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        MSA (MSA): Message Acknowledgment, required
        ERR (Optional[ERR]): Error, optional
        QAK (QAK): Query Acknowledgment, required
        QPD (QPD): Query Parameter Definition, required
        DONOR (Optional[RSP_O34_DONOR]): optional
        DONATION (Optional[RSP_O34_DONATION]): optional
    """

    pass
