"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: CCR_I17
Type: Message
"""
from __future__ import annotations

from .CCR_I16 import CCR_I16


class CCR_I17(CCR_I16):
    """Modify Collaborative Care Referral (S11.6.2).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        RF1 (List[RF1]): Referral Information, required
        PROVIDER_CONTACT (List[CCR_I16_PROVIDER_CONTACT]): required
        CLINICAL_ORDER (Optional[List[CCR_I16_CLINICAL_ORDER]]): optional
        PATIENT (List[CCR_I16_PATIENT]): required
        NK1 (Optional[List[NK1]]): Next of Kin / Associated Parties, optional
        INSURANCE (Optional[List[CCR_I16_INSURANCE]]): optional
        APPOINTMENT_HISTORY (Optional[List[CCR_I16_APPOINTMENT_HISTORY]]): optional
        CLINICAL_HISTORY (Optional[List[CCR_I16_CLINICAL_HISTORY]]): optional
        PATIENT_VISITS (List[CCR_I16_PATIENT_VISITS]): required
        MEDICATION_HISTORY (Optional[List[CCR_I16_MEDICATION_HISTORY]]): optional
        PROBLEM (Optional[List[CCR_I16_PROBLEM]]): optional
        GOAL (Optional[List[CCR_I16_GOAL]]): optional
        PATHWAY (Optional[List[CCR_I16_PATHWAY]]): optional
        REL (Optional[List[REL]]): Clinical Relationship Segment, optional
    """

    pass
