"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: ADT_A37
Type: Message
"""
from __future__ import annotations

from .ADT_A24 import ADT_A24


class ADT_A37(ADT_A24):
    """ADT/ACK -  Unlink patient information (S3.2.37).

    Attributes:
        MSH (MSH): Message header segment, required
        EVN (EVN): Event type, required
        PID (PID): Patient Identification, required
        PD1 (Optional[PD1]): Patient Demographic, optional
        PV1 (Optional[PV1]): Patient visit, optional
        DB1 (Optional[List[DB1]]): Disability Segment, optional
    """

    pass
