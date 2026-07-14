"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: CSU_C10
Type: Message
"""
from __future__ import annotations

from .CSU_C09 import CSU_C09


class CSU_C10(CSU_C09):
    """CSU - Patient completes the clinical trial (S7.7.2).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        PATIENT (List[CSU_C09_PATIENT]): required
    """

    pass
