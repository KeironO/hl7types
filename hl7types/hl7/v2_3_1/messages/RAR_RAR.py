"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: RAR_RAR
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.RAR_RAR_DEFINITION import RAR_RAR_DEFINITION
from ..segments.DSC import DSC
from ..segments.ERR import ERR
from ..segments.MSA import MSA
from ..segments.MSH import MSH

_DSC = DSC
_ERR = ERR
_MSA = MSA
_MSH = MSH
_RAR_RAR_DEFINITION = RAR_RAR_DEFINITION


class RAR_RAR(BaseModel):
    """HL7 v2 RAR_RAR message.

    Attributes:
        MSH (MSH): required
        MSA (MSA): required
        ERR (Optional[ERR]): optional
        DEFINITION (List[RAR_RAR_DEFINITION]): required
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

    DEFINITION: list[_RAR_RAR_DEFINITION] = Field(
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
