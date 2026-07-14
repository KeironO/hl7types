"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: PPR_PC3
Type: Message
"""
from __future__ import annotations

from .PPR_PC1 import PPR_PC1


class PPR_PC3(PPR_PC1):
    """PPR - PC/Problem Delete (S12.2.2).

    Attributes:
        MSH (MSH): Message header segment, required
        PID (PID): Patient Identification, required
        PATIENT_VISIT (Optional[PPR_PC1_PATIENT_VISIT]): optional
        PROBLEM (List[PPR_PC1_PROBLEM]): required
    """

    pass
