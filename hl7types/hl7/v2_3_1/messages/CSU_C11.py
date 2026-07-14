"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: CSU_C11
Type: Message
"""
from __future__ import annotations

from .CSU_C09 import CSU_C09


class CSU_C11(CSU_C09):
    """CSU - Patient completes a phase of the clinical trial (S7.6.2).

    Attributes:
        MSH (MSH): MSH - message header segment, required
        PATIENT (List[CSU_C09_PATIENT]): required
    """

    pass
