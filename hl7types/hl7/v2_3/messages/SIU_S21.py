"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: SIU_S21
Type: Message
"""
from __future__ import annotations

from .SIU_S12 import SIU_S12


class SIU_S21(SIU_S12):
    """SIU/ACK - Notification of discontinuation of service/resource on appointment (S10.3.10).

    Attributes:
        MSH (MSH): Message header segment, required
        SCH (SCH): Schedule Activity Information, required
        NTE (Optional[List[NTE]]): Notes and comments segment, optional
        PATIENT (Optional[List[SIU_S12_PATIENT]]): optional
        RESOURCES (List[SIU_S12_RESOURCES]): required
    """

    pass
