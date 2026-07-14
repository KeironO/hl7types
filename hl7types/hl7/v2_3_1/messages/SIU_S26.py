"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: SIU_S26
Type: Message
"""
from __future__ import annotations

from .SIU_S12 import SIU_S12


class SIU_S26(SIU_S12):
    """Notification that patient did not show up for schedule appointment (S10.3.14).

    Attributes:
        MSH (MSH): MSH - message header segment, required
        SCH (SCH): SCH - schedule activity information segment, required
        NTE (Optional[List[NTE]]): NTE - notes and comments segment, optional
        PATIENT (Optional[List[SIU_S12_PATIENT]]): optional
        RESOURCES (List[SIU_S12_RESOURCES]): required
    """

    pass
