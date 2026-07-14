"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: PGL_PC7
Type: Message
"""
from __future__ import annotations

from .PGL_PC6 import PGL_PC6


class PGL_PC7(PGL_PC6):
    """PGL - PC/ Goal Update.

    Attributes:
        MSH (MSH): MSH - message header segment, required
        PID (PID): PID - patient identification segment, required
        PATIENT_VISIT (Optional[PGL_PC6_PATIENT_VISIT]): optional
        GOAL (List[PGL_PC6_GOAL]): required
    """

    pass
