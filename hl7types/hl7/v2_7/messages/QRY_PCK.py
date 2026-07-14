"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: QRY_PCK
Type: Message
"""
from __future__ import annotations

from .QRY_PC4 import QRY_PC4


class QRY_PCK(QRY_PC4):
    """QRY - PC/ pathway (goal-oriented) query (S12.3.11).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        QRD (QRD): withdrawn, required
        QRF (Optional[QRF]): withdrawn, optional
    """

    pass
