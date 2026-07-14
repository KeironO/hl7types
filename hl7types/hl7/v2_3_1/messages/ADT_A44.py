"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: ADT_A44
Type: Message
"""
from __future__ import annotations

from .ADT_A43 import ADT_A43


class ADT_A44(ADT_A43):
    """ADT/ACK - Move account information - patient account number (S3.2.44).

    Attributes:
        MSH (MSH): MSH - message header segment, required
        EVN (EVN): EVN - event type segment, required
        PATIENT (List[ADT_A43_PATIENT]): required
    """

    pass
