"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: ADT_A37
Type: Message
"""
from __future__ import annotations

from .ADT_A24 import ADT_A24


class ADT_A37(ADT_A24):
    """ADT/ACK -  Unlink patient information (S3.2.37).

    Attributes:
        MSH (MSH): MSH - message header segment, required
        EVN (EVN): EVN - event type segment, required
        PID (PID): PID - patient identification segment, required
        PD1 (Optional[PD1]): PD1 - patient additional demographic segment, optional
        PV1 (Optional[PV1]): PV1 - patient visit segment-, optional
        DB1 (Optional[List[DB1]]): DB1 - Disability segment, optional
    """

    pass
