"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: ADT_A42
Type: Message
"""
from __future__ import annotations

from .ADT_A39 import ADT_A39


class ADT_A42(ADT_A39):
    """ADT/ACK - Merge visit - visit number (S3.2.42).

    Attributes:
        MSH (MSH): Message header segment, required
        EVN (EVN): Event type, required
        PATIENT (List[ADT_A39_PATIENT]): required
    """

    pass
