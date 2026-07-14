"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: QBP_Q25
Type: Message
"""
from __future__ import annotations

from .QBP_Q21 import QBP_Q21


class QBP_Q25(QBP_Q21):
    """QBP - Personnel Information by Segment Query (S15.3.7).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        QPD (QPD): Query Parameter Definition, required
        RCP (RCP): Response Control Parameter, required
        DSC (Optional[DSC]): Continuation Pointer, optional
    """

    pass
