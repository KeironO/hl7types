"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: MDM_T10
Type: Message
"""
from __future__ import annotations

from .MDM_T02 import MDM_T02


class MDM_T10(MDM_T02):
    """MDM/ACK - Document replacement notification and content (S9.6.10).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        EVN (EVN): Event Type, required
        PID (PID): Patient Identification, required
        PV1 (PV1): Patient Visit, required
        COMMON_ORDER (Optional[List[MDM_T02_COMMON_ORDER]]): optional
        TXA (TXA): Transcription Document Header, required
        CON (Optional[List[CON]]): Consent Segment, optional
        OBSERVATION (List[MDM_T02_OBSERVATION]): required
    """

    pass
