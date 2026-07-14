"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: ACK_R01
Type: Message
"""
from __future__ import annotations

from .ACK import ACK


class ACK_R01(ACK):
    """ORU/ACK - Unsolicited transmission of an observation message (S7.3.1).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        MSA (MSA): Message Acknowledgment, required
        ERR (Optional[List[ERR]]): Error, optional
    """

    pass
