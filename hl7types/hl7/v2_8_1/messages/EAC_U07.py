"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: EAC_U07
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.EAC_U07_COMMAND import EAC_U07_COMMAND
from ..segments.EQU import EQU
from ..segments.MSH import MSH
from ..segments.SFT import SFT
from ..segments.UAC import UAC

_EAC_U07_COMMAND = EAC_U07_COMMAND
_EQU = EQU
_MSH = MSH
_SFT = SFT
_UAC = UAC


class EAC_U07(BaseModel):
    """HL7 v2 EAC_U07 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        EQU (EQU): required
        COMMAND (List[EAC_U07_COMMAND]): required
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

    COMMAND: list[_EAC_U07_COMMAND] = Field(
        default=...,
        title="COMMAND",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
