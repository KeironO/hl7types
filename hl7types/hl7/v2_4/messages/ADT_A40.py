"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: ADT_A40
Type: Message
"""
from __future__ import annotations

from .ADT_A39 import ADT_A39


class ADT_A40(ADT_A39):
    """ADT/ACK - Merge patient - patient identifier list (S3.3.40).

    Attributes:
        MSH (MSH): Message Header, required
        EVN (EVN): Event Type, required
        PATIENT (List[ADT_A39_PATIENT]): required
    """

    pass
