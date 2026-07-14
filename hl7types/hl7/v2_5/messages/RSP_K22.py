"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: RSP_K22
Type: Message
"""
from __future__ import annotations

from .RSP_K21 import RSP_K21


class RSP_K22(RSP_K21):
    """RSP - Find candidates response (S3.3.57).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        MSA (MSA): Message Acknowledgment, required
        ERR (Optional[ERR]): Error, optional
        QAK (QAK): Query Acknowledgment, required
        QPD (QPD): Query Parameter Definition, required
        QUERY_RESPONSE (Optional[List[RSP_K21_QUERY_RESPONSE]]): optional
        DSC (Optional[DSC]): Continuation Pointer, optional
    """

    pass
