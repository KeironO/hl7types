"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: BAR_P05
Type: Message
"""
from __future__ import annotations

from .BAR_P01 import BAR_P01


class BAR_P05(BAR_P01):
    """BAR/ACK - Update account (S6.3.5).

    Attributes:
        MSH (MSH): Message header segment, required
        EVN (EVN): Event type, required
        PID (PID): Patient Identification, required
        PD1 (Optional[PD1]): Patient Demographic, optional
        VISIT (List[BAR_P01_VISIT]): required
    """

    pass
