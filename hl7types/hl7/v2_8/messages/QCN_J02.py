"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: QCN_J02
Type: Message
"""
from __future__ import annotations

from .QCN_J01 import QCN_J01


class QCN_J02(QCN_J01):
    """QSX/ACK - Cancel subscription/acknowledge message (S5.4.7).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        QID (QID): Query Identification, required
    """

    pass
