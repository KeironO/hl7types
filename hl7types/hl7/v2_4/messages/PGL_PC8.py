"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: PGL_PC8
Type: Message
"""
from __future__ import annotations

from .PGL_PC6 import PGL_PC6


class PGL_PC8(PGL_PC6):
    """PGL - PC/ Goal Delete (S12.3.1).

    Attributes:
        MSH (MSH): Message Header, required
        PID (PID): Patient identification, required
        PATIENT_VISIT (Optional[PGL_PC6_PATIENT_VISIT]): optional
        GOAL (List[PGL_PC6_GOAL]): required
    """

    pass
