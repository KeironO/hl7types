"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: PGL_PC8
Type: Message
"""
from __future__ import annotations

from .PGL_PC6 import PGL_PC6


class PGL_PC8(PGL_PC6):
    """PGL - PC/ goal delete (S12.3.1).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        PID (PID): Patient Identification, required
        PATIENT_VISIT (Optional[PGL_PC6_PATIENT_VISIT]): optional
        GOAL (List[PGL_PC6_GOAL]): required
    """

    pass
