"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: MDM_T08
Type: Message
"""
from __future__ import annotations

from .MDM_T02 import MDM_T02


class MDM_T08(MDM_T02):
    """MDM/ACK - Document edit notification and content (S9.4.8).

    Attributes:
        MSH (MSH): MSH - message header segment, required
        EVN (EVN): EVN - event type segment, required
        PID (PID): PID - patient identification segment, required
        PV1 (PV1): PV1 - patient visit segment-, required
        TXA (TXA): Document notification segment, required
        OBX (List[OBX]): OBX - observation/result segment, required
    """

    pass
