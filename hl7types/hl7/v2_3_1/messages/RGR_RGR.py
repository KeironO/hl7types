"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: RGR_RGR
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.RGR_RGR_DEFINITION import RGR_RGR_DEFINITION
from ..segments.DSC import DSC
from ..segments.ERR import ERR
from ..segments.MSA import MSA
from ..segments.MSH import MSH

_DSC = DSC
_ERR = ERR
_MSA = MSA
_MSH = MSH
_RGR_RGR_DEFINITION = RGR_RGR_DEFINITION


class RGR_RGR(BaseModel):
    """HL7 v2 RGR_RGR message.

    Attributes:
        MSH (MSH): required
        MSA (MSA): required
        ERR (Optional[ERR]): optional
        DEFINITION (List[RGR_RGR_DEFINITION]): required
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

    ERR: _ERR | None = Field(
        default=None,
        title="ERR",
        description="Optional",
    )

    DEFINITION: list[_RGR_RGR_DEFINITION] = Field(
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
