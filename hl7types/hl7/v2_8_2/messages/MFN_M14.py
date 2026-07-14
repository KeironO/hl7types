"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: MFN_M14
Type: Message
"""
from __future__ import annotations

from .MFN_Znn import MFN_Znn


class MFN_M14(MFN_Znn):
    """MFN/MFK - Master file notification - site defined (S8.4.3).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        MFI (MFI): Master File Identification, required
        MF_SITE_DEFINED (List[MFN_Znn_MF_SITE_DEFINED]): required
    """

    pass
