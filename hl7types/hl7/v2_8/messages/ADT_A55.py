"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: ADT_A55
Type: Message
"""
from __future__ import annotations

from .ADT_A54 import ADT_A54


class ADT_A55(ADT_A54):
    """ADT/ACK - Cancel change attending doctor (S3.3.55).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        EVN (EVN): Event Type, required
        PID (PID): Patient Identification, required
        PD1 (Optional[PD1]): Patient Additional Demographic, optional
        ROL (Optional[List[ROL]]): Role, optional
        PV1 (PV1): Patient Visit, required
        PV2 (Optional[PV2]): Patient Visit - Additional Information, optional
    """

    pass
