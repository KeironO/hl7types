"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: RQI_I07
Type: Message
"""
from __future__ import annotations

from .RQI_I01 import RQI_I01


class RQI_I07(RQI_I01):
    """PIN/ACK - Unsolicited insurance information (S11.3.7).

    Attributes:
        MSH (MSH): Message Header, required
        PROVIDER (List[RQI_I01_PROVIDER]): required
        PID (PID): Patient identification, required
        NK1 (Optional[List[NK1]]): Next of kin / associated parties, optional
        GUARANTOR_INSURANCE (Optional[RQI_I01_GUARANTOR_INSURANCE]): optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
    """

    pass
