"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: EAN_U09
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.EQU import EQU
from ..segments.MSH import MSH
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.EAN_U09_NOTIFICATION import EAN_U09_NOTIFICATION

_EAN_U09_NOTIFICATION = EAN_U09_NOTIFICATION
_EQU = EQU
_MSH = MSH
_SFT = SFT
_UAC = UAC


class EAN_U09(HL7Model):
    """EAN/ACK - Automated equipment notification (S13.3.9).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        EQU (EQU): Equipment Detail, required
        NOTIFICATION (List[EAN_U09_NOTIFICATION]): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message Header",
    )

    SFT: Optional[List[_SFT]] = Field(
        default=None,
        title="SFT",
        description="Software Segment",
    )

    UAC: Optional[_UAC] = Field(
        default=None,
        title="UAC",
        description="User Authentication Credential Segment",
    )

    EQU: _EQU = Field(
        title="EQU",
        description="Equipment Detail",
    )

    NOTIFICATION: List[_EAN_U09_NOTIFICATION] = Field(
        min_length=1,
        title="NOTIFICATION",
    )

    model_config = {"populate_by_name": True}
