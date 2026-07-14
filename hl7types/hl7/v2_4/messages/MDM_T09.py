"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: MDM_T09
Type: Message
"""
from __future__ import annotations

from .MDM_T01 import MDM_T01


class MDM_T09(MDM_T01):
    """MDM/ACK - Document replacement notification (S9.5.9).

    Attributes:
        MSH (MSH): Message Header, required
        EVN (EVN): Event Type, required
        PID (PID): Patient identification, required
        PV1 (PV1): Patient visit, required
        TXA (TXA): Transcription Document Header, required
    """

    pass
