"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: MFQ_M02
Type: Message
"""
from __future__ import annotations

from .MFQ_M01 import MFQ_M01


class MFQ_M02(MFQ_M01):
    """MFN/MFK - Master file - Staff Practitioner (S8.7.1).

    Attributes:
        MSH (MSH): Message Header, required
        QRD (QRD): Original-Style Query Definition, required
        QRF (Optional[QRF]): Original Style Query Filter, optional
        DSC (Optional[DSC]): Continuation Pointer, optional
    """

    pass
