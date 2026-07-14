"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: SRM_S09
Type: Message
"""
from __future__ import annotations

from .SRM_S01 import SRM_S01


class SRM_S09(SRM_S01):
    """SRM/SRR - Request cancellation of service/resource on appointment (S10.2.9).

    Attributes:
        MSH (MSH): MSH - message header segment, required
        ARQ (ARQ): ARQ - appointment request segment, required
        APR (Optional[APR]): APR - appointment preferences segment, optional
        NTE (Optional[List[NTE]]): NTE - notes and comments segment, optional
        PATIENT (Optional[List[SRM_S01_PATIENT]]): optional
        RESOURCES (List[SRM_S01_RESOURCES]): required
    """

    pass
