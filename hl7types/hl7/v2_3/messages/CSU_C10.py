"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: CSU_C10
Type: Message
"""
from __future__ import annotations

from .CSU_C09 import CSU_C09


class CSU_C10(CSU_C09):
    """CSU - Patient completes the clinical trial (S7.6.2).

    Attributes:
        MSH (MSH): Message header segment, required
        PATIENT (List[CSU_C09_PATIENT]): required
    """

    pass
