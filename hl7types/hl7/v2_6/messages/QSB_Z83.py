"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: QSB_Z83
Type: Message
"""
from __future__ import annotations

from .QSB_Q16 import QSB_Q16


class QSB_Z83(QSB_Q16):
    """ORU Subscription (S5.7.3.1).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        QPD (QPD): Query Parameter Definition, required
        RCP (RCP): Response Control Parameter, required
        DSC (Optional[DSC]): Continuation Pointer, optional
    """

    pass
