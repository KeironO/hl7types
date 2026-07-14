"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: ADT_A23
Type: Message
"""
from __future__ import annotations

from .ADT_A21 import ADT_A21


class ADT_A23(ADT_A21):
    """ADT/ACK -  Delete a patient record (S3.3.23).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        EVN (EVN): Event Type, required
        PID (PID): Patient Identification, required
        PD1 (Optional[PD1]): Patient Additional Demographic, optional
        PV1 (PV1): Patient Visit, required
        PV2 (Optional[PV2]): Patient Visit - Additional Information, optional
        DB1 (Optional[List[DB1]]): Disability, optional
        OBX (Optional[List[OBX]]): Observation/Result, optional
    """

    pass
