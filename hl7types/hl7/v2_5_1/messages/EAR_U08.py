"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: EAR_U08
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

from ..groups.EAR_U08_COMMAND_RESPONSE import EAR_U08_COMMAND_RESPONSE

_EAR_U08_COMMAND_RESPONSE = EAR_U08_COMMAND_RESPONSE
_EQU = EQU
_MSH = MSH
_ROL = ROL
_SFT = SFT


class EAR_U08(HL7Model):
    """HL7 v2 EAR_U08 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        EQU (EQU): required
        COMMAND_RESPONSE (List[EAR_U08_COMMAND_RESPONSE]): required
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

    COMMAND_RESPONSE: List[_EAR_U08_COMMAND_RESPONSE] = Field(
        min_length=1,
        title="COMMAND_RESPONSE",
        description="Required, repeating",
    )

    ROL: Optional[_ROL] = Field(
        default=None,
        title="ROL",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
