"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: ADT_A31
Type: Message
"""
from __future__ import annotations

from .ADT_A05 import ADT_A05


class ADT_A31(ADT_A05):
    """ADT/ACK -  Update person information (S3.3.31).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        EVN (EVN): Event Type, required
        PID (PID): Patient Identification, required
        PD1 (Optional[PD1]): Patient Additional Demographic, optional
        ARV (Optional[List[ARV]]): Access Restriction, optional
        ROL (Optional[List[ROL]]): Role, optional
        NK1 (Optional[List[NK1]]): Next of Kin / Associated Parties, optional
        PV1 (PV1): Patient Visit, required
        PV2 (Optional[PV2]): Patient Visit - Additional Information, optional
        DB1 (Optional[List[DB1]]): Disability, optional
        OBX (Optional[List[OBX]]): Observation/Result, optional
        AL1 (Optional[List[AL1]]): Patient Allergy Information, optional
        DG1 (Optional[List[DG1]]): Diagnosis, optional
        DRG (Optional[DRG]): Diagnosis Related Group, optional
        PROCEDURE (Optional[List[ADT_A05_PROCEDURE]]): optional
        GT1 (Optional[List[GT1]]): Guarantor, optional
        INSURANCE (Optional[List[ADT_A05_INSURANCE]]): optional
        ACC (Optional[ACC]): Accident, optional
        UB1 (Optional[UB1]): UB82, optional
        UB2 (Optional[UB2]): UB92 Data, optional
    """

    pass
