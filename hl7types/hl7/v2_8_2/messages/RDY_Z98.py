"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: RDY_Z98
Type: Message
"""
from __future__ import annotations

from .RDY_K15 import RDY_K15


class RDY_Z98(RDY_K15):
    """ (S5.9.5.1).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        MSA (MSA): Message Acknowledgment, required
        ERR (Optional[ERR]): Error, optional
        QAK (QAK): Query Acknowledgment, required
        QPD (QPD): Query Parameter Definition, required
        DSP (Optional[List[DSP]]): Display Data, optional
        DSC (Optional[DSC]): Continuation Pointer, optional
    """

    pass
