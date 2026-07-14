"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: PPG_PCJ
Type: Message
"""
from __future__ import annotations

from .PPG_PCG import PPG_PCG


class PPG_PCJ(PPG_PCG):
    """PPP - PC/Pathway (Goal Oriented) Delete (S12.2.4).

    Attributes:
        MSH (MSH): Message header segment, required
        PID (PID): Patient Identification, required
        PATIENT_VISIT (Optional[PPG_PCG_PATIENT_VISIT]): optional
        PATHWAY (List[PPG_PCG_PATHWAY]): required
    """

    pass
