"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: ADT_A51
Type: Message
"""
from __future__ import annotations

from .ADT_A50 import ADT_A50


class ADT_A51(ADT_A50):
    """ADT/ACK - Change alternate visit ID (S3.2.51).

    Attributes:
        MSH (MSH): MSH - message header segment, required
        EVN (EVN): EVN - event type segment, required
        PID (PID): PID - patient identification segment, required
        PD1 (Optional[PD1]): PD1 - patient additional demographic segment, optional
        MRG (MRG): MRG - merge patient information segment-, required
        PV1 (PV1): PV1 - patient visit segment-, required
    """

    pass
