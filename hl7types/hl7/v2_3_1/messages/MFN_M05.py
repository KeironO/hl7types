"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: MFN_M05
Type: Message
"""
from __future__ import annotations

from .MFN_M01 import MFN_M01


class MFN_M05(MFN_M01):
    """MFN/MFK - Patient location master file (S8).

    Attributes:
        MSH (MSH): MSH - message header segment, required
        MFI (MFI): MFI - master file identification segment, required
        MF (List[MFN_M01_MF]): required
    """

    pass
