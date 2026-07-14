"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: PPR_PC3
Type: Message
"""
from __future__ import annotations

from .PPR_PC1 import PPR_PC1


class PPR_PC3(PPR_PC1):
    """PPR - PC/ problem delete (S12.3.2).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        PID (PID): Patient Identification, required
        PATIENT_VISIT (Optional[PPR_PC1_PATIENT_VISIT]): optional
        PROBLEM (List[PPR_PC1_PROBLEM]): required
    """

    pass
