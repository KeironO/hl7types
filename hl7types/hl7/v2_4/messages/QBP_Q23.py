"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: QBP_Q23
Type: Message
"""
from __future__ import annotations

from .QBP_Q21 import QBP_Q21


class QBP_Q23(QBP_Q21):
    """QBP - Get corresponding identifiers (S3.3.58).

    Attributes:
        MSH (MSH): Message Header, required
        QPD (QPD): Query Parameter Definition, required
        RCP (RCP): Response Control Parameter, required
        DSC (Optional[DSC]): Continuation Pointer, optional
    """

    pass
