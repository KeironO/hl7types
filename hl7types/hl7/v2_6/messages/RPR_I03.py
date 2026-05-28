"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: RPR_I03
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.RPR_I03_PROVIDER import RPR_I03_PROVIDER
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.NTE import NTE
from ..segments.PID import PID
from ..segments.SFT import SFT
from ..segments.UAC import UAC

_MSA = MSA
_MSH = MSH
_NTE = NTE
_PID = PID
_RPR_I03_PROVIDER = RPR_I03_PROVIDER
_SFT = SFT
_UAC = UAC


class RPR_I03(BaseModel):
    """HL7 v2 RPR_I03 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        MSA (MSA): required
        PROVIDER (List[RPR_I03_PROVIDER]): required
        PID (Optional[List[PID]]): optional
        NTE (Optional[List[NTE]]): optional
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

    PROVIDER: list[_RPR_I03_PROVIDER] = Field(
        default=...,
        title="PROVIDER",
        description="Required, repeating",
    )

    PID: list[_PID] | None = Field(
        default=None,
        title="PID",
        description="Optional, repeating",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
