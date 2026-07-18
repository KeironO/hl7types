"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: SPQ_Q08
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

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


class SPQ_Q08(HL7Model):
    """HL7 v2 SPQ_Q08 message.

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        SPR (SPR): Stored Procedure Request Definition, required
        RDF (Optional[RDF]): Table Row Definition, optional
        DSC (Optional[DSC]): Continuation Pointer, optional
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

    SPR: _SPR = Field(
        title="SPR",
        description="Stored Procedure Request Definition",
    )

    RDF: Optional[_RDF] = Field(
        default=None,
        title="RDF",
        description="Table Row Definition",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="Continuation Pointer",
    )

    model_config = ConfigDict(populate_by_name=True)
