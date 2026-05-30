"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
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
    """HL7 v2 EAN_U09 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        EQU (EQU): required
        NOTIFICATION (List[EAN_U09_NOTIFICATION]): required
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    SFT: Optional[List[_SFT]] = Field(
        default=None,
        title="SFT",
        description="Optional, repeating",
    )

    UAC: Optional[_UAC] = Field(
        default=None,
        title="UAC",
        description="Optional",
    )

    EQU: _EQU = Field(
        default=...,
        title="EQU",
        description="Required",
    )

    NOTIFICATION: List[_EAN_U09_NOTIFICATION] = Field(
        default=...,
        title="NOTIFICATION",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
