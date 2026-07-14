"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: ADT_A34
Type: Message
"""
from __future__ import annotations

from .ADT_A30 import ADT_A30


class ADT_A34(ADT_A30):
    """ADT/ACK -  Merge patient information - patient ID only (S3.2.34).

    Attributes:
        MSH (MSH): Message header segment, required
        EVN (EVN): Event type, required
        PID (PID): Patient Identification, required
        PD1 (Optional[PD1]): Patient Demographic, optional
        MRG (MRG): Merge patient information, required
    """

    pass
