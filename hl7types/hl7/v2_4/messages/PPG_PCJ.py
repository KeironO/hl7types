"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: PPG_PCJ
Type: Message
"""
from __future__ import annotations

from .PPG_PCG import PPG_PCG


class PPG_PCJ(PPG_PCG):
    """PPG - PC/ Pathway (Goal-Oriented) Delete (S12.3.4).

    Attributes:
        MSH (MSH): Message Header, required
        PID (PID): Patient identification, required
        PATIENT_VISIT (Optional[PPG_PCG_PATIENT_VISIT]): optional
        PATHWAY (List[PPG_PCG_PATHWAY]): required
    """

    pass
