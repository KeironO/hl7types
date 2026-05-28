"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: EAR_U08
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.EAR_U08_COMMAND_RESPONSE import EAR_U08_COMMAND_RESPONSE
from ..segments.EQU import EQU
from ..segments.MSH import MSH
from ..segments.ROL import ROL
from ..segments.SFT import SFT
from ..segments.UAC import UAC

_EAR_U08_COMMAND_RESPONSE = EAR_U08_COMMAND_RESPONSE
_EQU = EQU
_MSH = MSH
_ROL = ROL
_SFT = SFT
_UAC = UAC


class EAR_U08(BaseModel):
    """HL7 v2 EAR_U08 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        EQU (EQU): required
        COMMAND_RESPONSE (List[EAR_U08_COMMAND_RESPONSE]): required
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

    COMMAND_RESPONSE: list[_EAR_U08_COMMAND_RESPONSE] = Field(
        default=...,
        title="COMMAND_RESPONSE",
        description="Required, repeating",
    )

    ROL: _ROL | None = Field(
        default=None,
        title="ROL",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
