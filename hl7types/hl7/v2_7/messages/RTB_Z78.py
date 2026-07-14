"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: RTB_Z78
Type: Message
"""
from __future__ import annotations

from .RTB_K13 import RTB_K13


class RTB_Z78(RTB_K13):
    """Tabular Patient List (Response) (S5.9.7.0).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        MSA (MSA): Message Acknowledgment, required
        ERR (Optional[ERR]): Error, optional
        QAK (QAK): Query Acknowledgment, required
        QPD (QPD): Query Parameter Definition, required
        ROW_DEFINITION (Optional[RTB_K13_ROW_DEFINITION]): optional
        DSC (Optional[DSC]): Continuation Pointer, optional
    """

    pass
