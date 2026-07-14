"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: PPG_PCH
Type: Message
"""
from __future__ import annotations

from .PPG_PCG import PPG_PCG


class PPG_PCH(PPG_PCG):
    """PPG - PC/ Pathway (Goal-Oriented) Update (S12.2.4).

    Attributes:
        MSH (MSH): MSH - message header segment, required
        PID (PID): PID - patient identification segment, required
        PATIENT_VISIT (Optional[PPG_PCG_PATIENT_VISIT]): optional
        PATHWAY (List[PPG_PCG_PATHWAY]): required
    """

    pass
