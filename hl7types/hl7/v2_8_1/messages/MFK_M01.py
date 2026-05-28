"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: MFK_M01
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

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


class MFK_M01(BaseModel):
    """HL7 v2 MFK_M01 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        MSA (MSA): required
        ERR (Optional[List[ERR]]): optional
        MFI (MFI): required
        MFA (Optional[List[MFA]]): optional
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

    MSA: _MSA = Field(
        default=...,
        title="MSA",
        description="Required",
    )

    ERR: list[_ERR] | None = Field(
        default=None,
        title="ERR",
        description="Optional, repeating",
    )

    MFI: _MFI = Field(
        default=...,
        title="MFI",
        description="Required",
    )

    MFA: list[_MFA] | None = Field(
        default=None,
        title="MFA",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
