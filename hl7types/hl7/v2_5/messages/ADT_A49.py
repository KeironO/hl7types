"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: ADT_A49
Type: Message
"""
from __future__ import annotations

from .ADT_A30 import ADT_A30


class ADT_A49(ADT_A30):
    """ADT/ACK - Change patient account number (S3.3.49).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        EVN (EVN): Event Type, required
        PID (PID): Patient Identification, required
        PD1 (Optional[PD1]): Patient Additional Demographic, optional
        MRG (MRG): Merge Patient Information, required
    """

    pass
