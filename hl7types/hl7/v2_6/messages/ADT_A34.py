"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: ADT_A34
Type: Message
"""
from __future__ import annotations

from .ADT_A30 import ADT_A30


class ADT_A34(ADT_A30):
    """ADT/ACK -  Merge patient information - patient ID only (for backward compatibili (S3.3.34).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        EVN (EVN): Event Type, required
        PID (PID): Patient Identification, required
        PD1 (Optional[PD1]): Patient Additional Demographic, optional
        ARV (Optional[List[ARV]]): Access Restriction, optional
        MRG (MRG): Merge Patient Information, required
    """

    pass
