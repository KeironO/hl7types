"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: ADT_A51
Type: Message
"""
from __future__ import annotations

from .ADT_A50 import ADT_A50


class ADT_A51(ADT_A50):
    """ADT/ACK - Change alternate visit ID (S3.3.51).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        EVN (EVN): Event Type, required
        PID (PID): Patient Identification, required
        PD1 (Optional[PD1]): Patient Additional Demographic, optional
        MRG (MRG): Merge Patient Information, required
        PV1 (PV1): Patient Visit, required
    """

    pass
