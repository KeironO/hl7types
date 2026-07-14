"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: QRY_Q26
Type: Message
"""
from __future__ import annotations

from .QRY_Q01 import QRY_Q01


class QRY_Q26(QRY_Q01):
    """pharmacy/treatment order query (S4.13.13).

    Attributes:
        MSH (MSH): Message Header, required
        QRD (QRD): Original-Style Query Definition, required
        QRF (Optional[QRF]): Original Style Query Filter, optional
        DSC (Optional[DSC]): Continuation Pointer, optional
    """

    pass
