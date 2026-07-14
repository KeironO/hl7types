"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: QBP_Z75
Type: Message
"""
from __future__ import annotations

from .QBP_Q13 import QBP_Q13


class QBP_Z75(QBP_Q13):
    """Tabular Patient List (S5.9.7.2).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        QPD (QPD): Query Parameter Definition, required
        RDF (Optional[RDF]): Table Row Definition, optional
        RCP (RCP): Response Control Parameter, required
        DSC (Optional[DSC]): Continuation Pointer, optional
    """

    pass
