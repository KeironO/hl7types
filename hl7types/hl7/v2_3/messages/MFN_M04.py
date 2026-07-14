"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: MFN_M04
Type: Message
"""
from __future__ import annotations

from .MFN_M06 import MFN_M06


class MFN_M04(MFN_M06):
    """MFN/MFK - Charge description master file (S8.9.1).

    Attributes:
        MSH (MSH): Message header segment, required
        MFI (MFI): Master file identification segment, required
        MF_CDM (List[MFN_M06_MF_CDM]): required
    """

    pass
