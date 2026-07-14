"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: VQQ_Q07
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


class VQQ_Q07(HL7Model):
    """VQQ - Virtual table query.

    Attributes:
        MSH (MSH): MSH - message header segment, required
        VTQ (VTQ): VTQ - virtual table query request segment, required
        RDF (Optional[RDF]): RDF - table row definition segment, optional
        DSC (Optional[DSC]): DSC - Continuation pointer segment, optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="MSH - message header segment",
    )

    VTQ: _VTQ = Field(
        title="VTQ",
        description="VTQ - virtual table query request segment",
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
