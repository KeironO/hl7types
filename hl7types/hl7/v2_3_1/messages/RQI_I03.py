"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: RQI_I03
Type: Message
"""
from __future__ import annotations

from .RQI_I01 import RQI_I01


class RQI_I03(RQI_I01):
    """RQI/RPR - Request/receipt of patient selection list (S11.2.3).

    Attributes:
        MSH (MSH): MSH - message header segment, required
        PROVIDER (List[RQI_I01_PROVIDER]): required
        PID (PID): PID - patient identification segment, required
        NK1 (Optional[List[NK1]]): NK1 - next of kin / associated parties segment-, optional
        GUARANTOR_INSURANCE (Optional[RQI_I01_GUARANTOR_INSURANCE]): optional
        NTE (Optional[List[NTE]]): NTE - notes and comments segment, optional
    """

    pass
