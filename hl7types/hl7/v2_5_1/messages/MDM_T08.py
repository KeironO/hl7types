"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: MDM_T08
Type: Message
"""
from __future__ import annotations

from .MDM_T02 import MDM_T02


class MDM_T08(MDM_T02):
    """MDM/ACK - Document edit notification and content (S9.5.8).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        EVN (EVN): Event Type, required
        PID (PID): Patient Identification, required
        PV1 (PV1): Patient Visit, required
        COMMON_ORDER (Optional[List[MDM_T02_COMMON_ORDER]]): optional
        TXA (TXA): Transcription Document Header, required
        OBXNTE_SUPPGRP (List[MDM_T02_OBXNTE_SUPPGRP]): required
    """

    pass
