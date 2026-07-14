"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: RDE_O25
Type: Message
"""
from __future__ import annotations

from .RDE_O11 import RDE_O11


class RDE_O25(RDE_O11):
    """RDE - Pharmacy/treatment refill authorization request (S4.A.13).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        PATIENT (Optional[RDE_O11_PATIENT]): optional
        ORDER (List[RDE_O11_ORDER]): required
    """

    pass
