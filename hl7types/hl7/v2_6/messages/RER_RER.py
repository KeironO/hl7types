"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: RER_RER
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.RER_RER_DEFINITION import RER_RER_DEFINITION
from ..segments.DSC import DSC
from ..segments.ERR import ERR
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.SFT import SFT
from ..segments.UAC import UAC

_DSC = DSC
_ERR = ERR
_MSA = MSA
_MSH = MSH
_RER_RER_DEFINITION = RER_RER_DEFINITION
_SFT = SFT
_UAC = UAC


class RER_RER(BaseModel):
    """HL7 v2 RER_RER message.

    Attributes:
        MSH (MSH): required
        MSA (MSA): required
        ERR (Optional[List[ERR]]): optional
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        DEFINITION (List[RER_RER_DEFINITION]): required
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

    ERR: list[_ERR] | None = Field(
        default=None,
        title="ERR",
        description="Optional, repeating",
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

    DEFINITION: list[_RER_RER_DEFINITION] = Field(
        default=...,
        title="DEFINITION",
        description="Required, repeating",
    )

    DSC: _DSC | None = Field(
        default=None,
        title="DSC",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
