"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: RQA_I09
Type: Message
"""
from __future__ import annotations

from .RQA_I08 import RQA_I08


class RQA_I09(RQA_I08):
    """RQA/RPA - Request for modification to an authorization (S11.3.3).

    Attributes:
        MSH (MSH): MSH - message header segment, required
        RF1 (Optional[RF1]): Referral Infomation, optional
        AUTHORIZATION (Optional[RQA_I08_AUTHORIZATION]): optional
        PROVIDER (List[RQA_I08_PROVIDER]): required
        PID (PID): PID - patient identification segment, required
        NK1 (Optional[List[NK1]]): NK1 - next of kin / associated parties segment-, optional
        GUARANTOR_INSURANCE (Optional[RQA_I08_GUARANTOR_INSURANCE]): optional
        ACC (Optional[ACC]): ACC - accident segment, optional
        DG1 (Optional[List[DG1]]): DG1 - diagnosis segment, optional
        DRG (Optional[List[DRG]]): DRG - diagnosis related group segment, optional
        AL1 (Optional[List[AL1]]): AL1 - patient allergy information segment, optional
        PROCEDURE (Optional[List[RQA_I08_PROCEDURE]]): optional
        OBSERVATION (Optional[List[RQA_I08_OBSERVATION]]): optional
        VISIT (Optional[RQA_I08_VISIT]): optional
        NTE (Optional[List[NTE]]): NTE - notes and comments segment, optional
    """

    pass
