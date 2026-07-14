"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: CRM_C08
Type: Message
"""
from __future__ import annotations

from .CRM_C01 import CRM_C01


class CRM_C08(CRM_C01):
    """CRM - Patient has gone off phase of clinical trial (S7.7.1).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        PATIENT (List[CRM_C01_PATIENT]): required
    """

    pass
