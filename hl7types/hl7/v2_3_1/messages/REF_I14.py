"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: REF_I14
Type: Message
"""
from __future__ import annotations

from .REF_I12 import REF_I12


class REF_I14(REF_I12):
    """REF/RRI - Cancel patient referral (S11.4.4).

    Attributes:
        MSH (MSH): MSH - message header segment, required
        RF1 (Optional[RF1]): Referral Infomation, optional
        AUTHORIZATION_CONTACT (Optional[REF_I12_AUTHORIZATION_CONTACT]): optional
        PROVIDER (List[REF_I12_PROVIDER]): required
        PID (PID): PID - patient identification segment, required
        NK1 (Optional[List[NK1]]): NK1 - next of kin / associated parties segment-, optional
        GT1 (Optional[List[GT1]]): GT1 - guarantor segment, optional
        INSURANCE (Optional[List[REF_I12_INSURANCE]]): optional
        ACC (Optional[ACC]): ACC - accident segment, optional
        DG1 (Optional[List[DG1]]): DG1 - diagnosis segment, optional
        DRG (Optional[List[DRG]]): DRG - diagnosis related group segment, optional
        AL1 (Optional[List[AL1]]): AL1 - patient allergy information segment, optional
        PROCEDURE (Optional[List[REF_I12_PROCEDURE]]): optional
        OBSERVATION (Optional[List[REF_I12_OBSERVATION]]): optional
        PATIENT_VISIT (Optional[REF_I12_PATIENT_VISIT]): optional
        NTE (Optional[List[NTE]]): NTE - notes and comments segment, optional
    """

    pass
