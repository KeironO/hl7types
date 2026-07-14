"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: ADT_A05
Type: Message
"""
from __future__ import annotations

from .ADT_A01 import ADT_A01


class ADT_A05(ADT_A01):
    """ADT/ACK -  Pre-admit a patient (S3.2.5).

    Attributes:
        MSH (MSH): MSH - message header segment, required
        EVN (EVN): EVN - event type segment, required
        PID (PID): PID - patient identification segment, required
        PD1 (Optional[PD1]): PD1 - patient additional demographic segment, optional
        NK1 (Optional[List[NK1]]): NK1 - next of kin / associated parties segment-, optional
        PV1 (PV1): PV1 - patient visit segment-, required
        PV2 (Optional[PV2]): PV2 - patient visit - additional information segment, optional
        DB1 (Optional[List[DB1]]): DB1 - Disability segment, optional
        OBX (Optional[List[OBX]]): OBX - observation/result segment, optional
        AL1 (Optional[List[AL1]]): AL1 - patient allergy information segment, optional
        DG1 (Optional[List[DG1]]): DG1 - diagnosis segment, optional
        DRG (Optional[DRG]): DRG - diagnosis related group segment, optional
        PROCEDURE (Optional[List[ADT_A01_PROCEDURE]]): optional
        GT1 (Optional[List[GT1]]): GT1 - guarantor segment, optional
        INSURANCE (Optional[List[ADT_A01_INSURANCE]]): optional
        ACC (Optional[ACC]): ACC - accident segment, optional
        UB1 (Optional[UB1]): UB1 - UB82 data segment, optional
        UB2 (Optional[UB2]): UB2 - UB92 data segment, optional
    """

    pass
