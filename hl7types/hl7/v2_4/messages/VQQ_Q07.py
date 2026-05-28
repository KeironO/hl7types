"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: VQQ_Q07
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.DSC import DSC
from ..segments.MSH import MSH
from ..segments.RDF import RDF
from ..segments.VTQ import VTQ

_DSC = DSC
_MSH = MSH
_RDF = RDF
_VTQ = VTQ


class VQQ_Q07(BaseModel):
    """HL7 v2 VQQ_Q07 message.

    Attributes:
        MSH (MSH): required
        VTQ (VTQ): required
        RDF (Optional[RDF]): optional
        DSC (Optional[DSC]): optional
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    VTQ: _VTQ = Field(
        default=...,
        title="VTQ",
        description="Required",
    )

    RDF: _RDF | None = Field(
        default=None,
        title="RDF",
        description="Optional",
    )

    DSC: _DSC | None = Field(
        default=None,
        title="DSC",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
