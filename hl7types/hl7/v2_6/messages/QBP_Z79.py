"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: QBP_Z79
Type: Message
"""
from __future__ import annotations

from .QBP_Q15 import QBP_Q15


class QBP_Z79(QBP_Q15):
    """Dispense Information (S5.9.6.1).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        QPD (QPD): Query Parameter Definition, required
        RCP (RCP): Response Control Parameter, required
        DSC (Optional[DSC]): Continuation Pointer, optional
    """

    pass
