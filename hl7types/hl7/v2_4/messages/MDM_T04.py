"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: MDM_T04
Type: Message
"""
from __future__ import annotations

from .MDM_T02 import MDM_T02


class MDM_T04(MDM_T02):
    """MDM/ACK - Document status change notification and content (S9.5.4).

    Attributes:
        MSH (MSH): Message Header, required
        EVN (EVN): Event Type, required
        PID (PID): Patient identification, required
        PV1 (PV1): Patient visit, required
        TXA (TXA): Transcription Document Header, required
        OBX (List[OBX]): Observation/Result, required
    """

    pass
