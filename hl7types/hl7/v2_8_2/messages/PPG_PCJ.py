"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: PPG_PCJ
Type: Message
"""
from __future__ import annotations

from .PPG_PCG import PPG_PCG


class PPG_PCJ(PPG_PCG):
    """PPG - PC/ pathway (goal-oriented) delete (S12.3.4).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        PID (PID): Patient Identification, required
        PATIENT_VISIT (Optional[PPG_PCG_PATIENT_VISIT]): optional
        PATHWAY (List[PPG_PCG_PATHWAY]): required
    """

    pass
