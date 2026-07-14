"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: ORU_R40
Type: Message
"""
from __future__ import annotations

from .ORU_R01 import ORU_R01


class ORU_R40(ORU_R01):
    """ORU - Unsolicited Report Alarm (S7.3.12).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        PATIENT_RESULT (List[ORU_R01_PATIENT_RESULT]): required
        DSC (Optional[DSC]): Continuation Pointer, optional
    """

    pass
