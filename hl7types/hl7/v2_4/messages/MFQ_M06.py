"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: MFQ_M06
Type: Message
"""
from __future__ import annotations

from .MFQ_M01 import MFQ_M01


class MFQ_M06(MFQ_M01):
    """MFN/MFK - Clinical study with phases and schedules master file (S8.11.1).

    Attributes:
        MSH (MSH): Message Header, required
        QRD (QRD): Original-Style Query Definition, required
        QRF (Optional[QRF]): Original Style Query Filter, optional
        DSC (Optional[DSC]): Continuation Pointer, optional
    """

    pass
