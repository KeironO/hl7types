"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: REF_I15
Type: Message
"""
from __future__ import annotations

from .REF_I12 import REF_I12


class REF_I15(REF_I12):
    """REF/RRI - Request patient referral status (S11.4.5).

    Attributes:
        MSH (MSH): Message header segment, required
        RF1 (Optional[RF1]): Referral Information Segment, optional
        AUTHORIZATION (Optional[REF_I12_AUTHORIZATION]): optional
        PROVIDER (List[REF_I12_PROVIDER]): required
        PID (PID): Patient Identification, required
        NK1 (Optional[List[NK1]]): Next of kin, optional
        GT1 (Optional[List[GT1]]): Guarantor, optional
        INSURANCE (Optional[List[REF_I12_INSURANCE]]): optional
        ACC (Optional[ACC]): Accident, optional
        DG1 (Optional[List[DG1]]): Diagnosis, optional
        DRG (Optional[List[DRG]]): Diagnosis Related Group, optional
        AL1 (Optional[List[AL1]]): Patient allergy information, optional
        PROCEDURE (Optional[List[REF_I12_PROCEDURE]]): optional
        RESULTS (Optional[List[REF_I12_RESULTS]]): optional
        VISIT (Optional[REF_I12_VISIT]): optional
        NTE (Optional[List[NTE]]): Notes and comments segment, optional
    """

    pass
