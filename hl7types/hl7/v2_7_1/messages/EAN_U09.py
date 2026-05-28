"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: EAN_U09
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.EAN_U09_NOTIFICATION import EAN_U09_NOTIFICATION
from ..segments.EQU import EQU
from ..segments.MSH import MSH
from ..segments.ROL import ROL
from ..segments.SFT import SFT
from ..segments.UAC import UAC

_EAN_U09_NOTIFICATION = EAN_U09_NOTIFICATION
_EQU = EQU
_MSH = MSH
_ROL = ROL
_SFT = SFT
_UAC = UAC


class EAN_U09(BaseModel):
    """HL7 v2 EAN_U09 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        EQU (EQU): required
        NOTIFICATION (List[EAN_U09_NOTIFICATION]): required
        ROL (Optional[ROL]): optional
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    SFT: list[_SFT] | None = Field(
        default=None,
        title="SFT",
        description="Optional, repeating",
    )

    UAC: _UAC | None = Field(
        default=None,
        title="UAC",
        description="Optional",
    )

    EQU: _EQU = Field(
        default=...,
        title="EQU",
        description="Required",
    )

    NOTIFICATION: list[_EAN_U09_NOTIFICATION] = Field(
        default=...,
        title="NOTIFICATION",
        description="Required, repeating",
    )

    ROL: _ROL | None = Field(
        default=None,
        title="ROL",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
