"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: PPP_PCD
Type: Message
"""
from __future__ import annotations

from .PPP_PCB import PPP_PCB


class PPP_PCD(PPP_PCB):
    """PPP - PC/ Pathway (Problem-Oriented) Delete (S12.3.3).

    Attributes:
        MSH (MSH): Message Header, required
        PID (PID): Patient identification, required
        PATIENT_VISIT (Optional[PPP_PCB_PATIENT_VISIT]): optional
        PATHWAY (List[PPP_PCB_PATHWAY]): required
    """

    pass
