"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: QBP_Q31
Type: Message
"""
from __future__ import annotations

from .QBP_Q11 import QBP_Q11


class QBP_Q31(QBP_Q11):
    """DBP - Dispense History (S4.13.20).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        QPD (QPD): Query Parameter Definition, required
        RCP (RCP): Response Control Parameter, required
        DSC (Optional[DSC]): Continuation Pointer, optional
    """

    pass
