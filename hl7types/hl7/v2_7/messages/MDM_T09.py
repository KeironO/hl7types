"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: MDM_T09
Type: Message
"""
from __future__ import annotations

from .MDM_T01 import MDM_T01


class MDM_T09(MDM_T01):
    """MDM/ACK - Document replacement notification (S9.6.9).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        EVN (EVN): Event Type, required
        PID (PID): Patient Identification, required
        PV1 (PV1): Patient Visit, required
        COMMON_ORDER (Optional[List[MDM_T01_COMMON_ORDER]]): optional
        TXA (TXA): Transcription Document Header, required
        CON (Optional[List[CON]]): Consent Segment, optional
    """

    pass
