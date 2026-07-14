"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: SIU_S26
Type: Message
"""
from __future__ import annotations

from .SIU_S12 import SIU_S12


class SIU_S26(SIU_S12):
    """Notification that patient did not show up for schedule appointment (S10.4.14).

    Attributes:
        MSH (MSH): Message Header, required
        SCH (SCH): Scheduling Activity Information, required
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        PATIENT (Optional[List[SIU_S12_PATIENT]]): optional
        RESOURCES (List[SIU_S12_RESOURCES]): required
    """

    pass
