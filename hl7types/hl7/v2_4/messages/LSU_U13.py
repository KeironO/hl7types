"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: LSU_U13
Type: Message
"""
from __future__ import annotations

from .LSU_U12 import LSU_U12


class LSU_U13(LSU_U12):
    """LSR/ACK - Automated equipment log/service request (S13.3.13).

    Attributes:
        MSH (MSH): Message Header, required
        EQU (EQU): Equipment Detail, required
        EQP (List[EQP]): Equipment/log Service, required
        ROL (Optional[ROL]): Role, optional
    """

    pass
