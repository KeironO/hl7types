"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: CRM_C06
Type: Message
"""
from __future__ import annotations

from .CRM_C01 import CRM_C01


class CRM_C06(CRM_C01):
    """CRM - Cancel patient entering a phase (clerical mistake) (S7.7.1).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        PATIENT (List[CRM_C01_PATIENT]): required
    """

    pass
