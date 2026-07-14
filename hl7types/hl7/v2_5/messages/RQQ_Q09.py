"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: RQQ_Q09
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.DSC import DSC
from ..segments.ERQ import ERQ
from ..segments.MSH import MSH
from ..segments.SFT import SFT

_DSC = DSC
_ERQ = ERQ
_MSH = MSH
_SFT = SFT


class RQQ_Q09(HL7Model):
    """HL7 v2 RQQ_Q09 message.

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        ERQ (ERQ): Event replay query, required
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

    ERQ: _ERQ = Field(
        title="ERQ",
        description="Event replay query",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="Continuation Pointer",
    )

    model_config = {"populate_by_name": True}
