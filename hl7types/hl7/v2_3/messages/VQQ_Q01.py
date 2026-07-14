"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: VQQ_Q01
Type: Message
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.DSC import DSC
from ..segments.MSH import MSH
from ..segments.RDF import RDF
from ..segments.VTQ import VTQ

_DSC = DSC
_MSH = MSH
_RDF = RDF
_VTQ = VTQ


class VQQ_Q01(HL7Model):
    """QRY/DSR - Query sent for immediate response.

    Attributes:
        MSH (MSH): Message header segment, required
        VTQ (VTQ): Virtual Table Query Request, required
        RDF (Optional[RDF]): Table Row Definition, optional
        DSC (Optional[DSC]): Continuation pointer segment, optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message header segment",
    )

    VTQ: _VTQ = Field(
        title="VTQ",
        description="Virtual Table Query Request",
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

    model_config = {"populate_by_name": True}
