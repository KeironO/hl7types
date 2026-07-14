"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
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
        QPD (QPD): Query Parameter Definition, required
        anyHL7Segment (Optional[anyHL7Segment]): optional
        RCP (RCP): Response Control Parameter, required
        DSC (Optional[DSC]): Continuation Pointer, optional
    """

    pass
