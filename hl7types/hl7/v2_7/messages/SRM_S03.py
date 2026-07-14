"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: SRM_S03
Type: Message
"""
from __future__ import annotations

from .SRM_S01 import SRM_S01


class SRM_S03(SRM_S01):
    """SRM/SRR - Request appointment modification (S10.3).

    Attributes:
        MSH (MSH): Message Header, required
        ARQ (ARQ): Appointment Request, required
        APR (Optional[APR]): Appointment Preferences, optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        PATIENT (Optional[List[SRM_S01_PATIENT]]): optional
        RESOURCES (List[SRM_S01_RESOURCES]): required
    """

    pass
