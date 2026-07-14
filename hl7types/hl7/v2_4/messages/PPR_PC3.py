"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: PPR_PC3
Type: Message
"""
from __future__ import annotations

from .PPR_PC1 import PPR_PC1


class PPR_PC3(PPR_PC1):
    """PPR - PC/ Problem Delete (S12.3.2).

    Attributes:
        MSH (MSH): Message Header, required
        PID (PID): Patient identification, required
        PATIENT_VISIT (Optional[PPR_PC1_PATIENT_VISIT]): optional
        PROBLEM (List[PPR_PC1_PROBLEM]): required
    """

    pass
