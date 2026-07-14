"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: QBP_Q34
Type: Message
"""
from __future__ import annotations

from .QBP_O34 import QBP_O34


class QBP_Q34(QBP_O34):
    """ (S4.16.8).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        QPD (QPD): Query Parameter Definition, required
        RCP (RCP): Response Control Parameter, required
    """

    pass
