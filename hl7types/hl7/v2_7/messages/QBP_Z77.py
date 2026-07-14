"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: QBP_Z77
Type: Message
"""
from __future__ import annotations

from .QBP_Q13 import QBP_Q13


class QBP_Z77(QBP_Q13):
    """Tabular Patient List (S5.9.7.0).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        QPD (QPD): Query Parameter Definition, required
        QBP (Optional[QBP_Q13_QBP]): optional
        RDF (Optional[RDF]): Table Row Definition, optional
        RCP (RCP): Response Control Parameter, required
        DSC (Optional[DSC]): Continuation Pointer, optional
    """

    pass
