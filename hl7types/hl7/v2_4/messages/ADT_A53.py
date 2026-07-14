"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: ADT_A53
Type: Message
"""
from __future__ import annotations

from .ADT_A52 import ADT_A52


class ADT_A53(ADT_A52):
    """ADT/ACK - Cancel patient returns from a leave of absence (S3.3.53).

    Attributes:
        MSH (MSH): Message Header, required
        EVN (EVN): Event Type, required
        PID (PID): Patient identification, required
        PD1 (Optional[PD1]): patient additional demographic, optional
        PV1 (PV1): Patient visit, required
        PV2 (Optional[PV2]): Patient visit - additional information, optional
    """

    pass
