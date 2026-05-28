"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: ORA_R33
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.ERR import ERR
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.ORC import ORC
from ..segments.SFT import SFT
from ..segments.UAC import UAC

_ERR = ERR
_MSA = MSA
_MSH = MSH
_ORC = ORC
_SFT = SFT
_UAC = UAC


class ORA_R33(BaseModel):
    """HL7 v2 ORA_R33 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        MSA (MSA): required
        ERR (Optional[List[ERR]]): optional
        ORC (Optional[ORC]): optional
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

    ORC: _ORC | None = Field(
        default=None,
        title="ORC",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
