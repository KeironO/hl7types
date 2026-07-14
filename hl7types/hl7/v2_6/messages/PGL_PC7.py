"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: PGL_PC7
Type: Message
"""
from __future__ import annotations

from .PGL_PC6 import PGL_PC6


class PGL_PC7(PGL_PC6):
    """PGL - PC/ goal update (S12.3.1).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        PID (PID): Patient Identification, required
        PATIENT_VISIT (Optional[PGL_PC6_PATIENT_VISIT]): optional
        GOAL (List[PGL_PC6_GOAL]): required
    """

    pass
