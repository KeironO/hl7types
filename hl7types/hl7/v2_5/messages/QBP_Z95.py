"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: QBP_Z95
Type: Message
"""
from __future__ import annotations

from .QBP_Q13 import QBP_Q13


class QBP_Z95(QBP_Q13):
    """Tabular Dispense History (S5.9.4.1.1).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        QPD (QPD): Query Parameter Definition, required
        RDF (Optional[RDF]): Table Row Definition, optional
        RCP (RCP): Response Control Parameter, required
        DSC (Optional[DSC]): Continuation Pointer, optional
    """

    pass
