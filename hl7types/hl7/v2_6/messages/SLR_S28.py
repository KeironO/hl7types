"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: SLR_S28
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH
from ..segments.SFT import SFT
from ..segments.SLT import SLT
from ..segments.UAC import UAC

_MSH = MSH
_SFT = SFT
_SLT = SLT
_UAC = UAC


class SLR_S28(HL7Model):
    """SLR/SLS - Request new sterilization lot (S17.5.1).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        SLT (List[SLT]): Sterilization Lot, required
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

    UAC: Optional[_UAC] = Field(
        default=None,
        title="UAC",
        description="User Authentication Credential Segment",
    )

    SLT: List[_SLT] = Field(
        min_length=1,
        title="SLT",
        description="Sterilization Lot",
    )

    model_config = {"populate_by_name": True}
