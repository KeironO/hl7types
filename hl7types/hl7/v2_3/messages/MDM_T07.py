"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: MDM_T07
Type: Message
"""
from __future__ import annotations

from .MDM_T01 import MDM_T01


class MDM_T07(MDM_T01):
    """MDM/ACK - Document edit notification (S9.4.7).

    Attributes:
        MSH (MSH): Message header segment, required
        EVN (EVN): Event type, required
        PID (PID): Patient Identification, required
        PV1 (PV1): Patient visit, required
        TXA (TXA): Document notification segment, required
    """

    pass
