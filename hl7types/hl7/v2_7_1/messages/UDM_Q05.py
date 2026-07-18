"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: UDM_Q05
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.DSC import DSC
from ..segments.DSP import DSP
from ..segments.MSH import MSH
from ..segments.SFT import SFT
from ..segments.UAC import UAC
from ..segments.URD import URD
from ..segments.URS import URS

_DSC = DSC
_DSP = DSP
_MSH = MSH
_SFT = SFT
_UAC = UAC
_URD = URD
_URS = URS


class UDM_Q05(HL7Model):
    """UDM/ACK - Unsolicited display update message (S5.10.1.1).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        URD (URD): deleted, required
        URS (Optional[URS]): deleted, optional
        DSP (List[DSP]): Display Data, required
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

    UAC: Optional[_UAC] = Field(
        default=None,
        title="UAC",
        description="User Authentication Credential Segment",
    )

    URD: _URD = Field(
        title="URD",
        description="deleted",
    )

    URS: Optional[_URS] = Field(
        default=None,
        title="URS",
        description="deleted",
    )

    DSP: List[_DSP] = Field(
        min_length=1,
        title="DSP",
        description="Display Data",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="Continuation Pointer",
    )

    model_config = ConfigDict(populate_by_name=True)
