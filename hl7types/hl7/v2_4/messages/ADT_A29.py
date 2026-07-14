"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: ADT_A29
Type: Message
"""
from __future__ import annotations

from .ADT_A21 import ADT_A21


class ADT_A29(ADT_A21):
    """ADT/ACK -  Delete person information (S3.3.29).

    Attributes:
        MSH (MSH): Message Header, required
        EVN (EVN): Event Type, required
        PID (PID): Patient identification, required
        PD1 (Optional[PD1]): patient additional demographic, optional
        PV1 (PV1): Patient visit, required
        PV2 (Optional[PV2]): Patient visit - additional information, optional
        DB1 (Optional[List[DB1]]): Disability, optional
        OBX (Optional[List[OBX]]): Observation/Result, optional
    """

    pass
