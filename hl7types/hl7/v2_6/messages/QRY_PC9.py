"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: QRY_PC9
Type: Message
"""
from __future__ import annotations

from .QRY_PC4 import QRY_PC4


class QRY_PC9(QRY_PC4):
    """QRY - PC/ goal query (S12.3.7).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        QRD (QRD): Original-Style Query Definition, required
        QRF (Optional[QRF]): Original style query filter, optional
    """

    pass
