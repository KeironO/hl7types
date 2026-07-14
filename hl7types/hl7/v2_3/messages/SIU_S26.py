"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: SIU_S26
Type: Message
"""
from __future__ import annotations

from .SIU_S12 import SIU_S12


class SIU_S26(SIU_S12):
    """notification that patient did not show up for schedule appointment (S10.3.14).

    Attributes:
        MSH (MSH): Message header segment, required
        SCH (SCH): Schedule Activity Information, required
        NTE (Optional[List[NTE]]): Notes and comments segment, optional
        PATIENT (Optional[List[SIU_S12_PATIENT]]): optional
        RESOURCES (List[SIU_S12_RESOURCES]): required
    """

    pass
