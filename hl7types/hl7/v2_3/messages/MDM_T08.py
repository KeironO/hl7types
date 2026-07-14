"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: MDM_T08
Type: Message
"""
from __future__ import annotations

from .MDM_T02 import MDM_T02


class MDM_T08(MDM_T02):
    """MDM/ACK - Document edit notification and content (S9.4.8).

    Attributes:
        MSH (MSH): Message header segment, required
        EVN (EVN): Event type, required
        PID (PID): Patient Identification, required
        PV1 (PV1): Patient visit, required
        TXA (TXA): Document notification segment, required
        OBX (List[OBX]): Observation segment, required
    """

    pass
