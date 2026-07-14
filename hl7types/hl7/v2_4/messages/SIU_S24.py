"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: SIU_S24
Type: Message
"""
from __future__ import annotations

from .SIU_S12 import SIU_S12


class SIU_S24(SIU_S12):
    """SIU/ACK - Notification of opened (\"unblocked\"\") schedule time slot(s)\" (S10.4.13).

    Attributes:
        MSH (MSH): Message Header, required
        SCH (SCH): Scheduling Activity Information, required
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        PATIENT (Optional[List[SIU_S12_PATIENT]]): optional
        RESOURCES (List[SIU_S12_RESOURCES]): required
    """

    pass
