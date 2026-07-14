"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: SIU_S14
Type: Message
"""
from __future__ import annotations

from .SIU_S12 import SIU_S12


class SIU_S14(SIU_S12):
    """SIU/ACK - Notification of appointment modification (S10.4).

    Attributes:
        MSH (MSH): Message Header, required
        SCH (SCH): Scheduling Activity Information, required
        TQ1 (Optional[List[TQ1]]): Timing/Quantity, optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        PATIENT (Optional[List[SIU_S12_PATIENT]]): optional
        RESOURCES (List[SIU_S12_RESOURCES]): required
    """

    pass
