"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: ADT_A44
Type: Message
"""
from __future__ import annotations

from .ADT_A43 import ADT_A43


class ADT_A44(ADT_A43):
    """ADT/ACK - Move account information - internal ID (S3.2.44).

    Attributes:
        MSH (MSH): Message header segment, required
        EVN (EVN): Event type, required
        PATIENT (List[ADT_A43_PATIENT]): required
    """

    pass
