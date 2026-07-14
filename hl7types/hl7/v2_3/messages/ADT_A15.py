"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: ADT_A15
Type: Message
"""
from __future__ import annotations

from .ADT_A09 import ADT_A09


class ADT_A15(ADT_A09):
    """ADT/ACK -  Pending transfer (S3.2.15).

    Attributes:
        MSH (MSH): Message header segment, required
        EVN (EVN): Event type, required
        PID (PID): Patient Identification, required
        PD1 (Optional[PD1]): Patient Demographic, optional
        PV1 (PV1): Patient visit, required
        PV2 (Optional[PV2]): Patient visit - additional information, optional
        DB1 (Optional[List[DB1]]): Disability Segment, optional
        OBX (Optional[List[OBX]]): Observation segment, optional
        DG1 (Optional[List[DG1]]): Diagnosis, optional
    """

    pass
