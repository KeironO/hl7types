"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: ADT_A28
Type: Message
"""
from __future__ import annotations

from .ADT_A01 import ADT_A01


class ADT_A28(ADT_A01):
    """ADT/ACK -  Add person information (S3.2.28).

    Attributes:
        MSH (MSH): Message header segment, required
        EVN (EVN): Event type, required
        PID (PID): Patient Identification, required
        PD1 (Optional[PD1]): Patient Demographic, optional
        NK1 (Optional[List[NK1]]): Next of kin, optional
        PV1 (PV1): Patient visit, required
        PV2 (Optional[PV2]): Patient visit - additional information, optional
        DB1 (Optional[List[DB1]]): Disability Segment, optional
        OBX (Optional[List[OBX]]): Observation segment, optional
        AL1 (Optional[List[AL1]]): Patient allergy information, optional
        DG1 (Optional[List[DG1]]): Diagnosis, optional
        DRG (Optional[DRG]): Diagnosis Related Group, optional
        PROCEDURE (Optional[List[ADT_A01_PROCEDURE]]): optional
        GT1 (Optional[List[GT1]]): Guarantor, optional
        INSURANCE (Optional[List[ADT_A01_INSURANCE]]): optional
        ACC (Optional[ACC]): Accident, optional
        UB1 (Optional[UB1]): UB82  data, optional
        UB2 (Optional[UB2]): UB92 data, optional
    """

    pass
