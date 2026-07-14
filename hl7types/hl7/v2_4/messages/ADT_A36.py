"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: ADT_A36
Type: Message
"""
from __future__ import annotations

from .ADT_A30 import ADT_A30


class ADT_A36(ADT_A30):
    """ADT/ACK -  Merge patient information - patient ID and account number (S3.3.36).

    Attributes:
        MSH (MSH): Message Header, required
        EVN (EVN): Event Type, required
        PID (PID): Patient identification, required
        PD1 (Optional[PD1]): patient additional demographic, optional
        MRG (MRG): Merge patient information, required
    """

    pass
