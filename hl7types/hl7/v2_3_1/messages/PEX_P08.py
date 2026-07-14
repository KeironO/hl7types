"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: PEX_P08
Type: Message
"""
from __future__ import annotations

from .PEX_P07 import PEX_P07


class PEX_P08(PEX_P07):
    """PEX - Unsolicited update individual product experience report (S7.10.1).

    Attributes:
        MSH (MSH): MSH - message header segment, required
        EVN (EVN): EVN - event type segment, required
        PID (PID): PID - patient identification segment, required
        PD1 (Optional[PD1]): PD1 - patient additional demographic segment, optional
        NTE (Optional[List[NTE]]): NTE - notes and comments segment, optional
        VISIT (Optional[PEX_P07_VISIT]): optional
        EXPERIENCE (List[PEX_P07_EXPERIENCE]): required
    """

    pass
