"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: MFQ_M05
Type: Message
"""
from __future__ import annotations

from .MFQ_M01 import MFQ_M01


class MFQ_M05(MFQ_M01):
    """MFN/MFK - Patient location master file (S8).

    Attributes:
        MSH (MSH): MSH - message header segment, required
        QRD (QRD): QRD - original-style query definition segment, required
        QRF (Optional[QRF]): QRF - original style query filter segment, optional
        DSC (Optional[DSC]): DSC - Continuation pointer segment, optional
    """

    pass
