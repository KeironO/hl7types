"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: RPL_I02
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.RPL_I02_PROVIDER import RPL_I02_PROVIDER
from ..segments.DSC import DSC
from ..segments.DSP import DSP
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.NTE import NTE

_DSC = DSC
_DSP = DSP
_MSA = MSA
_MSH = MSH
_NTE = NTE
_RPL_I02_PROVIDER = RPL_I02_PROVIDER


class RPL_I02(BaseModel):
    """HL7 v2 RPL_I02 message.

    Attributes:
        MSH (MSH): required
        MSA (MSA): required
        PROVIDER (List[RPL_I02_PROVIDER]): required
        NTE (Optional[List[NTE]]): optional
        DSP (Optional[List[DSP]]): optional
        DSC (Optional[DSC]): optional
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    MSA: _MSA = Field(
        default=...,
        title="MSA",
        description="Required",
    )

    PROVIDER: list[_RPL_I02_PROVIDER] = Field(
        default=...,
        title="PROVIDER",
        description="Required, repeating",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    DSP: list[_DSP] | None = Field(
        default=None,
        title="DSP",
        description="Optional, repeating",
    )

    DSC: _DSC | None = Field(
        default=None,
        title="DSC",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
