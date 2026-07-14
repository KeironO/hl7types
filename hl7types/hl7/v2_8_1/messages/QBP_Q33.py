"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: QBP_Q33
Type: Message
"""
from __future__ import annotations

from .QBP_O33 import QBP_O33


class QBP_Q33(QBP_O33):
    """ (S4.16.6).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        QPD (QPD): Query Parameter Definition, required
        RCP (RCP): Response Control Parameter, required
    """

    pass
