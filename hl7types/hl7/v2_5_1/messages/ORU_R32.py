"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: ORU_R32
Type: Message
"""
from __future__ import annotations

from .ORU_R30 import ORU_R30


class ORU_R32(ORU_R30):
    """ORU - Unsolicited Pre-Ordered Point-Of-Care Observation (S7.3.6).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        PID (PID): Patient Identification, required
        PD1 (Optional[PD1]): Patient Additional Demographic, optional
        VISIT (Optional[ORU_R30_VISIT]): optional
        ORC (ORC): Common Order, required
        OBR (OBR): Observation Request, required
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        TIMING_QTY (Optional[List[ORU_R30_TIMING_QTY]]): optional
        OBSERVATION (List[ORU_R30_OBSERVATION]): required
    """

    pass
