"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: RSP_K33
Type: Message
"""
from __future__ import annotations

from .RSP_O33 import RSP_O33


class RSP_K33(RSP_O33):
    """Get Donor Record Candidates Response Message (S4.16.7).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        MSA (MSA): Message Acknowledgment, required
        ERR (Optional[ERR]): Error, optional
        QAK (QAK): Query Acknowledgment, required
        QPD (QPD): Query Parameter Definition, required
        DONOR (Optional[RSP_O33_DONOR]): optional
    """

    pass
