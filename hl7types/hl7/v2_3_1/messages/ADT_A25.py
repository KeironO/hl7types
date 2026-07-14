"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: ADT_A25
Type: Message
"""
from __future__ import annotations

from .ADT_A02 import ADT_A02


class ADT_A25(ADT_A02):
    """ADT/ACK -  Cancel pending discharge (S3.2.25).

    Attributes:
        MSH (MSH): MSH - message header segment, required
        EVN (EVN): EVN - event type segment, required
        PID (PID): PID - patient identification segment, required
        PD1 (Optional[PD1]): PD1 - patient additional demographic segment, optional
        PV1 (PV1): PV1 - patient visit segment-, required
        PV2 (Optional[PV2]): PV2 - patient visit - additional information segment, optional
        DB1 (Optional[List[DB1]]): DB1 - Disability segment, optional
        OBX (Optional[List[OBX]]): OBX - observation/result segment, optional
    """

    pass
