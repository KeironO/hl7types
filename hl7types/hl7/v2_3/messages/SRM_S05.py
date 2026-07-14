"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: SRM_S05
Type: Message
"""
from __future__ import annotations

from .SRM_S01 import SRM_S01


class SRM_S05(SRM_S01):
    """SRM/SRR - Request appointment discontinuation (S10.2.5).

    Attributes:
        MSH (MSH): Message header segment, required
        ARQ (ARQ): Appointment Request, required
        APR (Optional[APR]): Appointment Preferences, optional
        NTE (Optional[List[NTE]]): Notes and comments segment, optional
        PATIENT (Optional[List[SRM_S01_PATIENT]]): optional
        RESOURCES (List[SRM_S01_RESOURCES]): required
    """

    pass
