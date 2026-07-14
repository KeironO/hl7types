"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: RRE_O26
Type: Message
"""
from __future__ import annotations

from .RRE_O12 import RRE_O12


class RRE_O26(RRE_O12):
    """RRE - Pharmacy/Treatment Refill Authorization Acknowledgement (S4.A.14).

    Attributes:
        MSH (MSH): Message Header, required
        MSA (MSA): Message Acknowledgment, required
        ERR (Optional[List[ERR]]): Error, optional
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        RESPONSE (Optional[RRE_O12_RESPONSE]): optional
    """

    pass
