"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: PEX_P08
Type: Message
"""
from __future__ import annotations

from .PEX_P07 import PEX_P07


class PEX_P08(PEX_P07):
    """PEX - Unsolicited update individual product experience report (S7.11.1).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        EVN (EVN): Event Type, required
        PID (PID): Patient Identification, required
        PD1 (Optional[PD1]): Patient Additional Demographic, optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        VISIT (Optional[PEX_P07_VISIT]): optional
        EXPERIENCE (List[PEX_P07_EXPERIENCE]): required
    """

    pass
