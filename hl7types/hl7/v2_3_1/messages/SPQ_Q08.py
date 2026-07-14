"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: SPQ_Q08
Type: Message
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.DSC import DSC
from ..segments.MSH import MSH
from ..segments.RDF import RDF
from ..segments.SPR import SPR

_DSC = DSC
_MSH = MSH
_RDF = RDF
_SPR = SPR


class SPQ_Q08(HL7Model):
    """SPQ - Stored procedure request.

    Attributes:
        MSH (MSH): MSH - message header segment, required
        SPR (SPR): SPR - stored procedure request definition segment, required
        RDF (Optional[RDF]): RDF - table row definition segment, optional
        DSC (Optional[DSC]): DSC - Continuation pointer segment, optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="MSH - message header segment",
    )

    SPR: _SPR = Field(
        title="SPR",
        description="SPR - stored procedure request definition segment",
    )

    RDF: Optional[_RDF] = Field(
        default=None,
        title="RDF",
        description="RDF - table row definition segment",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="DSC - Continuation pointer segment",
    )

    model_config = {"populate_by_name": True}
