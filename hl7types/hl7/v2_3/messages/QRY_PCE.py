"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: QRY_PCE
Type: Message
"""
from __future__ import annotations

from .QRY_PC4 import QRY_PC4


class QRY_PCE(QRY_PC4):
    """PPP - PC/Pathway (Problem Oriented) Query (S12.2.9).

    Attributes:
        MSH (MSH): Message header segment, required
        QRD (QRD): Query definition segment, required
        QRF (Optional[QRF]): Query filter segment, optional
    """

    pass
