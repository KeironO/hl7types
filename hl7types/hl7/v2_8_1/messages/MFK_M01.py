"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: MFK_M01
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.ERR import ERR
from ..segments.MFA import MFA
from ..segments.MFI import MFI
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.SFT import SFT
from ..segments.UAC import UAC

_ERR = ERR
_MFA = MFA
_MFI = MFI
_MSA = MSA
_MSH = MSH
_SFT = SFT
_UAC = UAC


class MFK_M01(HL7Model):
    """HL7 v2 MFK_M01 message.

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        MSA (MSA): Message Acknowledgment, required
        ERR (Optional[List[ERR]]): Error, optional
        MFI (MFI): Master File Identification, required
        MFA (Optional[List[MFA]]): Master File Acknowledgment, optional
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

    MSA: _MSA = Field(
        title="MSA",
        description="Message Acknowledgment",
    )

    ERR: Optional[List[_ERR]] = Field(
        default=None,
        title="ERR",
        description="Error",
    )

    MFI: _MFI = Field(
        title="MFI",
        description="Master File Identification",
    )

    MFA: Optional[List[_MFA]] = Field(
        default=None,
        title="MFA",
        description="Master File Acknowledgment",
    )

    model_config = {"populate_by_name": True}
