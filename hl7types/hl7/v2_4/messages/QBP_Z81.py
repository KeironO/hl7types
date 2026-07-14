"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: QBP_Z81
Type: Message
"""
from __future__ import annotations

from .QBP_Q11 import QBP_Q11


class QBP_Z81(QBP_Q11):
    """Dispense History (S5.9.1.1.1).

    Attributes:
        MSH (MSH): Message Header, required
        QPD (QPD): Query Parameter Definition, required
        RCP (RCP): Response Control Parameter, required
        DSC (Optional[DSC]): Continuation Pointer, optional
    """

    pass
