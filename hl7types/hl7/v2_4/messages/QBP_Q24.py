"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: QBP_Q24
Type: Message
"""
from __future__ import annotations

from .QBP_Q21 import QBP_Q21


class QBP_Q24(QBP_Q21):
    """QBP - Allocate identifiers (S3.3.59).

    Attributes:
        MSH (MSH): Message Header, required
        QPD (QPD): Query Parameter Definition, required
        RCP (RCP): Response Control Parameter, required
        DSC (Optional[DSC]): Continuation Pointer, optional
    """

    pass
