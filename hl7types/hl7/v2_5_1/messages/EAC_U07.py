"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: EAC_U07
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.EQU import EQU
from ..segments.MSH import MSH
from ..segments.ROL import ROL
from ..segments.SFT import SFT

from ..groups.EAC_U07_COMMAND import EAC_U07_COMMAND

_EAC_U07_COMMAND = EAC_U07_COMMAND
_EQU = EQU
_MSH = MSH
_ROL = ROL
_SFT = SFT


class EAC_U07(HL7Model):
    """HL7 v2 EAC_U07 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        EQU (EQU): required
        COMMAND (List[EAC_U07_COMMAND]): required
        ROL (Optional[ROL]): optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Required",
    )

    SFT: Optional[List[_SFT]] = Field(
        default=None,
        title="SFT",
        description="Optional, repeating",
    )

    EQU: _EQU = Field(
        title="EQU",
        description="Required",
    )

    COMMAND: List[_EAC_U07_COMMAND] = Field(
        min_length=1,
        title="COMMAND",
        description="Required, repeating",
    )

    ROL: Optional[_ROL] = Field(
        default=None,
        title="ROL",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
