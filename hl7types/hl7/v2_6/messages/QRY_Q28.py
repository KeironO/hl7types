"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: QRY_Q28
Type: Message
"""
from __future__ import annotations

from .QRY_Q01 import QRY_Q01


class QRY_Q28(QRY_Q01):
    """RDR - Pharmacy/treatment dispense information (S4.13.17).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        QRD (QRD): Original-Style Query Definition, required
        QRF (Optional[QRF]): Original style query filter, optional
        DSC (Optional[DSC]): Continuation Pointer, optional
    """

    pass
