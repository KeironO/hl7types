"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: RQI_I02
Type: Message
"""
from __future__ import annotations

from .RQI_I01 import RQI_I01


class RQI_I02(RQI_I01):
    """RQI/RPL - Request/receipt of patient selection display list (S11.2.2).

    Attributes:
        MSH (MSH): Message header segment, required
        PROVIDER (List[RQI_I01_PROVIDER]): required
        PID (PID): Patient Identification, required
        NK1 (Optional[List[NK1]]): Next of kin, optional
        GUARANTOR_INSURANCE (Optional[RQI_I01_GUARANTOR_INSURANCE]): optional
        NTE (Optional[List[NTE]]): Notes and comments segment, optional
    """

    pass
