"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: RSP_K24
Type: Message
"""
from __future__ import annotations

from .RSP_K23 import RSP_K23


class RSP_K24(RSP_K23):
    """RSP - Allocate identifiers response (S3.3.59).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        MSA (MSA): Message Acknowledgment, required
        ERR (Optional[ERR]): Error, optional
        QAK (QAK): Query Acknowledgment, required
        QPD (QPD): Query Parameter Definition, required
        QUERY_RESPONSE (Optional[RSP_K23_QUERY_RESPONSE]): optional
        DSC (Optional[DSC]): Continuation Pointer, optional
    """

    pass
