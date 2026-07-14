"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: CSU_C12
Type: Message
"""
from __future__ import annotations

from .CSU_C09 import CSU_C09


class CSU_C12(CSU_C09):
    """CSU - Update/correction of patient order/result information (S7.7.2).

    Attributes:
        MSH (MSH): Message Header, required
        PATIENT (List[CSU_C09_PATIENT]): required
    """

    pass
