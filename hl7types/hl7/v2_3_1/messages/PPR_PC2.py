"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: PPR_PC2
Type: Message
"""
from __future__ import annotations

from .PPR_PC1 import PPR_PC1


class PPR_PC2(PPR_PC1):
    """PPR - PC/ Problem Update.

    Attributes:
        MSH (MSH): MSH - message header segment, required
        PID (PID): PID - patient identification segment, required
        PATIENT_VISIT (Optional[PPR_PC1_PATIENT_VISIT]): optional
        PROBLEM (List[PPR_PC1_PROBLEM]): required
    """

    pass
