"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: QRY_PCK
Type: Message
"""
from __future__ import annotations

from .QRY_PC4 import QRY_PC4


class QRY_PCK(QRY_PC4):
    """PTU - PC/ Pathway (Goal-Oriented) Query (S12.3.11).

    Attributes:
        MSH (MSH): Message Header, required
        QRD (QRD): Original-Style Query Definition, required
        QRF (Optional[QRF]): Original Style Query Filter, optional
    """

    pass
