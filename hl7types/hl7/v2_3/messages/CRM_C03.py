"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: CRM_C03
Type: Message
"""
from __future__ import annotations

from .CRM_C01 import CRM_C01


class CRM_C03(CRM_C01):
    """SRM - Correct/update registration information (S7.6.1).

    Attributes:
        MSH (MSH): Message header segment, required
        PATIENT (List[CRM_C01_PATIENT]): required
    """

    pass
