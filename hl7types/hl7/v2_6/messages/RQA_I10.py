"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: RQA_I10
Type: Message
"""
from __future__ import annotations

from .RQA_I08 import RQA_I08


class RQA_I10(RQA_I08):
    """RQA/RPA - Request for resubmission of an authorization (S11.4.1).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        RF1 (Optional[RF1]): Referral Information, optional
        AUTHORIZATION (Optional[RQA_I08_AUTHORIZATION]): optional
        PROVIDER (List[RQA_I08_PROVIDER]): required
        PID (PID): Patient Identification, required
        NK1 (Optional[List[NK1]]): Next of Kin / Associated Parties, optional
        GUARANTOR_INSURANCE (Optional[RQA_I08_GUARANTOR_INSURANCE]): optional
        ACC (Optional[ACC]): Accident, optional
        DG1 (Optional[List[DG1]]): Diagnosis, optional
        DRG (Optional[List[DRG]]): Diagnosis Related Group, optional
        AL1 (Optional[List[AL1]]): Patient Allergy Information, optional
        PROCEDURE (Optional[List[RQA_I08_PROCEDURE]]): optional
        OBSERVATION (Optional[List[RQA_I08_OBSERVATION]]): optional
        VISIT (Optional[RQA_I08_VISIT]): optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
    """

    pass
