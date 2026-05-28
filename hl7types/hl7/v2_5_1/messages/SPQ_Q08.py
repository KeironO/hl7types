"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: SPQ_Q08
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.DSC import DSC
from ..segments.MSH import MSH
from ..segments.RDF import RDF
from ..segments.SFT import SFT
from ..segments.SPR import SPR

_DSC = DSC
_MSH = MSH
_RDF = RDF
_SFT = SFT
_SPR = SPR


class SPQ_Q08(BaseModel):
    """HL7 v2 SPQ_Q08 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        SPR (SPR): required
        RDF (Optional[RDF]): optional
        DSC (Optional[DSC]): optional
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    SFT: Optional[List[_SFT]] = Field(
        default=None,
        title="SFT",
        description="Optional, repeating",
    )

    SPR: _SPR = Field(
        default=...,
        title="SPR",
        description="Required",
    )

    RDF: Optional[_RDF] = Field(
        default=None,
        title="RDF",
        description="Optional",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
