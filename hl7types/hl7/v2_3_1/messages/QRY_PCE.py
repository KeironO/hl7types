"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: QRY_PCE
Type: Message
"""
from __future__ import annotations

from .QRY_PC4 import QRY_PC4


class QRY_PCE(QRY_PC4):
    """PTQ - PC/ Pathway (Problem-Oriented) Query (S12.2.9).

    Attributes:
        MSH (MSH): MSH - message header segment, required
        QRD (QRD): QRD - original-style query definition segment, required
        QRF (Optional[QRF]): QRF - original style query filter segment, optional
    """

    pass
