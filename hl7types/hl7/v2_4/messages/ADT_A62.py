"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: ADT_A62
Type: Message
"""
from __future__ import annotations

from .ADT_A61 import ADT_A61


class ADT_A62(ADT_A61):
    """ADT/ACK - Cancel change consulting doctor (S3.3.62).

    Attributes:
        MSH (MSH): Message Header, required
        EVN (EVN): Event Type, required
        PID (PID): Patient identification, required
        PD1 (Optional[PD1]): patient additional demographic, optional
        PV1 (PV1): Patient visit, required
        ROL (Optional[List[ROL]]): Role, optional
        PV2 (Optional[PV2]): Patient visit - additional information, optional
    """

    pass
