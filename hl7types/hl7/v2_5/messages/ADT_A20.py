"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: ADT_A20
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.EVN import EVN
from ..segments.MSH import MSH
from ..segments.NPU import NPU
from ..segments.SFT import SFT

_EVN = EVN
_MSH = MSH
_NPU = NPU
_SFT = SFT


class ADT_A20(HL7Model):
    """ADT/ACK -  Bed status update (S3.3.1).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        EVN (EVN): Event Type, required
        NPU (NPU): Bed Status Update, required
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

    EVN: _EVN = Field(
        title="EVN",
        description="Event Type",
    )

    NPU: _NPU = Field(
        title="NPU",
        description="Bed Status Update",
    )

    model_config = {"populate_by_name": True}
