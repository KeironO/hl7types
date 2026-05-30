"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: VQQ_Q07
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.DSC import DSC
from ..segments.MSH import MSH
from ..segments.RDF import RDF
from ..segments.SFT import SFT
from ..segments.VTQ import VTQ

_DSC = DSC
_MSH = MSH
_RDF = RDF
_SFT = SFT
_VTQ = VTQ


class VQQ_Q07(HL7Model):
    """HL7 v2 VQQ_Q07 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        VTQ (VTQ): required
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

    VTQ: _VTQ = Field(
        default=...,
        title="VTQ",
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
