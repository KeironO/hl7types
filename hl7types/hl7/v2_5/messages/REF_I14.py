"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: REF_I14
Type: Message
"""
from __future__ import annotations

from .REF_I12 import REF_I12


class REF_I14(REF_I12):
    """REF/RRI - Cancel patient referral (S11.5.1).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        RF1 (Optional[RF1]): Referral Information, optional
        AUTHORIZATION_CONTACT (Optional[REF_I12_AUTHORIZATION_CONTACT]): optional
        PROVIDER_CONTACT (List[REF_I12_PROVIDER_CONTACT]): required
        PID (PID): Patient Identification, required
        NK1 (Optional[List[NK1]]): Next of Kin / Associated Parties, optional
        GT1 (Optional[List[GT1]]): Guarantor, optional
        INSURANCE (Optional[List[REF_I12_INSURANCE]]): optional
        ACC (Optional[ACC]): Accident, optional
        DG1 (Optional[List[DG1]]): Diagnosis, optional
        DRG (Optional[List[DRG]]): Diagnosis Related Group, optional
        AL1 (Optional[List[AL1]]): Patient Allergy Information, optional
        PROCEDURE (Optional[List[REF_I12_PROCEDURE]]): optional
        OBSERVATION (Optional[List[REF_I12_OBSERVATION]]): optional
        PATIENT_VISIT (Optional[REF_I12_PATIENT_VISIT]): optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
    """

    pass
