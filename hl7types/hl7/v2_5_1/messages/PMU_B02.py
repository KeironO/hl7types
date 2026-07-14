"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: PMU_B02
Type: Message
"""
from __future__ import annotations

from .PMU_B01 import PMU_B01


class PMU_B02(PMU_B01):
    """PMU/ACK - Update personnel record (S15.3.2).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        EVN (EVN): Event Type, required
        STF (STF): Staff Identification, required
        PRA (Optional[List[PRA]]): Practitioner Detail, optional
        ORG (Optional[List[ORG]]): Practitioner Organization Unit, optional
        AFF (Optional[List[AFF]]): Professional Affiliation, optional
        LAN (Optional[List[LAN]]): Language Detail, optional
        EDU (Optional[List[EDU]]): Educational Detail, optional
        CER (Optional[List[CER]]): Certificate Detail, optional
    """

    pass
