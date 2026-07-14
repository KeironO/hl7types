"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: MDM_T05
Type: Message
"""
from __future__ import annotations

from .MDM_T01 import MDM_T01


class MDM_T05(MDM_T01):
    """MDM/ACK - Document addendum notification (S9.4.5).

    Attributes:
        MSH (MSH): MSH - message header segment, required
        EVN (EVN): EVN - event type segment, required
        PID (PID): PID - patient identification segment, required
        PV1 (PV1): PV1 - patient visit segment-, required
        TXA (TXA): Document notification segment, required
    """

    pass
