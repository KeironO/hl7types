"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: SPQ_Q01
Type: Message
"""
from __future__ import annotations

from typing import Optional
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.DSC import DSC
from ..segments.MSH import MSH
from ..segments.RDF import RDF
from ..segments.SPR import SPR

_DSC = DSC
_MSH = MSH
_RDF = RDF
_SPR = SPR


class SPQ_Q01(HL7Model):
    """QRY/DSR - Query sent for immediate response.

    Attributes:
        MSH (MSH): Message header segment, required
        SPR (SPR): Stored Procedure Request Definition, required
        RDF (Optional[RDF]): Table Row Definition, optional
        DSC (Optional[DSC]): Continuation pointer segment, optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message header segment",
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
        description="Continuation pointer segment",
    )

    model_config = ConfigDict(populate_by_name=True)
