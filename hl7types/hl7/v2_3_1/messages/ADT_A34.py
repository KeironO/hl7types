"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: ADT_A34
Type: Message
"""
from __future__ import annotations

from .ADT_A30 import ADT_A30


class ADT_A34(ADT_A30):
    """ADT/ACK -  Merge patient information - patient ID only (S3.2.34).

    Attributes:
        MSH (MSH): MSH - message header segment, required
        EVN (EVN): EVN - event type segment, required
        PID (PID): PID - patient identification segment, required
        PD1 (Optional[PD1]): PD1 - patient additional demographic segment, optional
        MRG (MRG): MRG - merge patient information segment-, required
    """

    pass
