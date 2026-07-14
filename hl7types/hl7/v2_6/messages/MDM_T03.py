"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: MDM_T03
Type: Message
"""
from __future__ import annotations

from .MDM_T01 import MDM_T01


class MDM_T03(MDM_T01):
    """MDM/ACK - Document status change notification (S9.5.3).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        EVN (EVN): Event Type, required
        PID (PID): Patient Identification, required
        PV1 (PV1): Patient Visit, required
        COMMON_ORDER (Optional[List[MDM_T01_COMMON_ORDER]]): optional
        TXA (TXA): Transcription Document Header, required
    """

    pass
