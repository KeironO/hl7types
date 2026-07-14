"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: QBP_Znn
Type: Message
"""
from __future__ import annotations

from .QBP_Q11 import QBP_Q11


class QBP_Znn(QBP_Q11):
    """ (S5.3.2.3).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        QPD (QPD): Query Parameter Definition, required
        QBP (Optional[QBP_Q11_QBP]): optional
        RCP (RCP): Response Control Parameter, required
        DSC (Optional[DSC]): Continuation Pointer, optional
    """

    pass
