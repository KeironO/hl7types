"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: ADT_A11
Type: Message
"""
from __future__ import annotations

from .ADT_A09 import ADT_A09


class ADT_A11(ADT_A09):
    """ADT/ACK -  Cancel admit/visit notification (S3.3.11).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        EVN (EVN): Event Type, required
        PID (PID): Patient Identification, required
        PD1 (Optional[PD1]): Patient Additional Demographic, optional
        PV1 (PV1): Patient Visit, required
        PV2 (Optional[PV2]): Patient Visit - Additional Information, optional
        DB1 (Optional[List[DB1]]): Disability, optional
        OBX (Optional[List[OBX]]): Observation/Result, optional
        DG1 (Optional[List[DG1]]): Diagnosis, optional
    """

    pass
