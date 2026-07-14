"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: QRY_Q30
Type: Message
"""
from __future__ import annotations

from .QRY_Q01 import QRY_Q01


class QRY_Q30(QRY_Q01):
    """RGR - Pharmacy/treatment dose information (S4.13.19).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        QRD (QRD): Original-Style Query Definition, required
        QRF (Optional[QRF]): Original style query filter, optional
        DSC (Optional[DSC]): Continuation Pointer, optional
    """

    pass
