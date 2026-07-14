"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: ADT_A62
Type: Message
"""
from __future__ import annotations

from .ADT_A61 import ADT_A61


class ADT_A62(ADT_A61):
    """ADT/ACK - Cancel change consulting doctor (S3.3.62).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        EVN (EVN): Event Type, required
        PID (PID): Patient Identification, required
        PD1 (Optional[PD1]): Patient Additional Demographic, optional
        PV1 (PV1): Patient Visit, required
        ROL (Optional[List[ROL]]): Role, optional
        PV2 (Optional[PV2]): Patient Visit - Additional Information, optional
    """

    pass
