"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: RSP_Z84
Type: Message
"""
from __future__ import annotations

from .RSP_K11 import RSP_K11


class RSP_Z84(RSP_K11):
    """Who Am I (Response) (S5.3.1.1).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        MSA (MSA): Message Acknowledgment, required
        ERR (Optional[ERR]): Error, optional
        QAK (QAK): Query Acknowledgment, required
        QPD (QPD): Query Parameter Definition, required
        SEGMENT_PATTERN (Optional[RSP_K11_SEGMENT_PATTERN]): optional
        DSC (Optional[DSC]): Continuation Pointer, optional
    """

    pass
