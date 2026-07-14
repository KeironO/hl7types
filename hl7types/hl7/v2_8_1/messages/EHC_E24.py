"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: EHC_E24
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.ERR import ERR
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.EHC_E24_AUTHORIZATION_RESPONSE_INFO import EHC_E24_AUTHORIZATION_RESPONSE_INFO

_EHC_E24_AUTHORIZATION_RESPONSE_INFO = EHC_E24_AUTHORIZATION_RESPONSE_INFO
_ERR = ERR
_MSA = MSA
_MSH = MSH
_SFT = SFT
_UAC = UAC


class EHC_E24(HL7Model):
    """Authorization Response (S16.3.1).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[List[UAC]]): User Authentication Credential Segment, optional
        MSA (MSA): Message Acknowledgment, required
        ERR (Optional[List[ERR]]): Error, optional
        AUTHORIZATION_RESPONSE_INFO (EHC_E24_AUTHORIZATION_RESPONSE_INFO): required
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

    UAC: Optional[List[_UAC]] = Field(
        default=None,
        title="UAC",
        description="User Authentication Credential Segment",
    )

    MSA: _MSA = Field(
        title="MSA",
        description="Message Acknowledgment",
    )

    ERR: Optional[List[_ERR]] = Field(
        default=None,
        title="ERR",
        description="Error",
    )

    AUTHORIZATION_RESPONSE_INFO: _EHC_E24_AUTHORIZATION_RESPONSE_INFO = Field(
        title="AUTHORIZATION_RESPONSE_INFO",
    )

    model_config = {"populate_by_name": True}
