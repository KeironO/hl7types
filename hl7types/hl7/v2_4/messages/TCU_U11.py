"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: TCU_U11
Type: Message
"""
from __future__ import annotations

from .TCU_U10 import TCU_U10


class TCU_U11(TCU_U10):
    """TCR/ACK - Automated equipment test code settings request (S13.3.11).

    Attributes:
        MSH (MSH): Message Header, required
        EQU (EQU): Equipment Detail, required
        TCC (List[TCC]): Test Code Configuration, required
        ROL (Optional[ROL]): Role, optional
    """

    pass
