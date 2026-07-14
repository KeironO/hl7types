"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: MFQ_M07
Type: Message
"""
from __future__ import annotations

from .MFQ_M01 import MFQ_M01


class MFQ_M07(MFQ_M01):
    """MFN/MFK - Clinical study without phases but with schedules master file (S8.11.1).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        QRD (QRD): Original-Style Query Definition, required
        QRF (Optional[QRF]): Original style query filter, optional
        DSC (Optional[DSC]): Continuation Pointer, optional
    """

    pass
