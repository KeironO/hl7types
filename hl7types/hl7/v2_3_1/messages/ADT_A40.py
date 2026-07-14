"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: ADT_A40
Type: Message
"""
from __future__ import annotations

from .ADT_A39 import ADT_A39


class ADT_A40(ADT_A39):
    """ADT/ACK - Merge patient - internal ID (S3.2.40).

    Attributes:
        MSH (MSH): MSH - message header segment, required
        EVN (EVN): EVN - event type segment, required
        PATIENT (List[ADT_A39_PATIENT]): required
    """

    pass
