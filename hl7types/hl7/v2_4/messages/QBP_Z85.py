"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: QBP_Z85
Type: Message
"""
from __future__ import annotations

from .QBP_Q11 import QBP_Q11


class QBP_Z85(QBP_Q11):
    """Pharmacy Information Comprehensive (S5.9.1.2.1).

    Attributes:
        MSH (MSH): Message Header, required
        QPD (QPD): Query Parameter Definition, required
        RCP (RCP): Response Control Parameter, required
        DSC (Optional[DSC]): Continuation Pointer, optional
    """

    pass
