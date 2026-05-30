"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: ROR_ROR
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.DSC import DSC
from ..segments.ERR import ERR
from ..segments.MSA import MSA
from ..segments.MSH import MSH

from ..groups.ROR_ROR_DEFINITION import ROR_ROR_DEFINITION

_DSC = DSC
_ERR = ERR
_MSA = MSA
_MSH = MSH
_ROR_ROR_DEFINITION = ROR_ROR_DEFINITION


class ROR_ROR(HL7Model):
    """HL7 v2 ROR_ROR message.

    Attributes:
        MSH (MSH): required
        MSA (MSA): required
        ERR (Optional[ERR]): optional
        DEFINITION (List[ROR_ROR_DEFINITION]): required
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

    ERR: Optional[_ERR] = Field(
        default=None,
        title="ERR",
        description="Optional",
    )

    DEFINITION: List[_ROR_ROR_DEFINITION] = Field(
        default=...,
        title="DEFINITION",
        description="Required, repeating",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
