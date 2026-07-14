"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: ADT_A41
Type: Message
"""
from __future__ import annotations

from .ADT_A39 import ADT_A39


class ADT_A41(ADT_A39):
    """ADT/ACK - Merge account - patient account number (S3.2.41).

    Attributes:
        MSH (MSH): Message header segment, required
        EVN (EVN): Event type, required
        PATIENT (List[ADT_A39_PATIENT]): required
    """

    pass
