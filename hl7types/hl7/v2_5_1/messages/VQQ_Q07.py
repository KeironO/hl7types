"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: VQQ_Q07
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
from ..segments.VTQ import VTQ

_DSC = DSC
_MSH = MSH
_RDF = RDF
_SFT = SFT
_VTQ = VTQ


class VQQ_Q07(HL7Model):
    """HL7 v2 VQQ_Q07 message.

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        VTQ (VTQ): Virtual Table Query Request, required
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
        description="Continuation Pointer",
    )

    model_config = ConfigDict(populate_by_name=True)
