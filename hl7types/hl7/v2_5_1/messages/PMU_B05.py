"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: PMU_B05
Type: Message
"""
from __future__ import annotations

from .PMU_B04 import PMU_B04


class PMU_B05(PMU_B04):
    """PMU/ACK - Deactivate practicing person (S15.3.5).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        EVN (EVN): Event Type, required
        STF (STF): Staff Identification, required
        PRA (Optional[List[PRA]]): Practitioner Detail, optional
        ORG (Optional[List[ORG]]): Practitioner Organization Unit, optional
    """

    pass
