"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: ADT_A22
Type: Message
"""
from __future__ import annotations

from .ADT_A02 import ADT_A02


class ADT_A22(ADT_A02):
    """ADT/ACK -  Leave of absence - in (returning) (S3.2.22).

    Attributes:
        MSH (MSH): Message header segment, required
        EVN (EVN): Event type, required
        PID (PID): Patient Identification, required
        PD1 (Optional[PD1]): Patient Demographic, optional
        PV1 (PV1): Patient visit, required
        PV2 (Optional[PV2]): Patient visit - additional information, optional
        DB1 (Optional[List[DB1]]): Disability Segment, optional
        OBX (Optional[List[OBX]]): Observation segment, optional
    """

    pass
