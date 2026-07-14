"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: EAR_U08
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

from ..groups.EAR_U08_COMMAND_RESPONSE import EAR_U08_COMMAND_RESPONSE

_EAR_U08_COMMAND_RESPONSE = EAR_U08_COMMAND_RESPONSE
_EQU = EQU
_MSH = MSH
_SFT = SFT
_UAC = UAC


class EAR_U08(HL7Model):
    """EAR/ACK - Automated equipment response (S13.3.8).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        EQU (EQU): Equipment Detail, required
        COMMAND_RESPONSE (List[EAR_U08_COMMAND_RESPONSE]): required
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

    COMMAND_RESPONSE: List[_EAR_U08_COMMAND_RESPONSE] = Field(
        min_length=1,
        title="COMMAND_RESPONSE",
    )

    model_config = {"populate_by_name": True}
