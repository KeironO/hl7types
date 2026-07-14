"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: CRM_C05
Type: Message
"""
from __future__ import annotations

from .CRM_C01 import CRM_C01


class CRM_C05(CRM_C01):
    """CRM - Patient enters phase of clinical trial (S7.6.1).

    Attributes:
        MSH (MSH): MSH - message header segment, required
        PATIENT (List[CRM_C01_PATIENT]): required
    """

    pass
