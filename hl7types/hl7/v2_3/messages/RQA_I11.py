"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: RQA_I11
Type: Message
"""
from __future__ import annotations

from .RQA_I08 import RQA_I08


class RQA_I11(RQA_I08):
    """RQA/RPA - Request for cancellation of an authorization (S11.4).

    Attributes:
        MSH (MSH): Message header segment, required
        RF1 (Optional[RF1]): Referral Information Segment, optional
        AUTHORIZATION (Optional[RQA_I08_AUTHORIZATION]): optional
        PROVIDER (List[RQA_I08_PROVIDER]): required
        PID (PID): Patient Identification, required
        NK1 (Optional[List[NK1]]): Next of kin, optional
        GUARANTOR_INSURANCE (Optional[RQA_I08_GUARANTOR_INSURANCE]): optional
        ACC (Optional[ACC]): Accident, optional
        DG1 (Optional[List[DG1]]): Diagnosis, optional
        DRG (Optional[List[DRG]]): Diagnosis Related Group, optional
        AL1 (Optional[List[AL1]]): Patient allergy information, optional
        PROCEDURE (Optional[List[RQA_I08_PROCEDURE]]): optional
        OBSERVATION (Optional[List[RQA_I08_OBSERVATION]]): optional
        VISIT (Optional[RQA_I08_VISIT]): optional
        NTE (Optional[List[NTE]]): Notes and comments segment, optional
    """

    pass
