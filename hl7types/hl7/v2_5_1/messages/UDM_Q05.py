"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
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
from ..segments.URD import URD
from ..segments.URS import URS

_DSC = DSC
_DSP = DSP
_MSH = MSH
_SFT = SFT
_URD = URD
_URS = URS


class UDM_Q05(HL7Model):
    """HL7 v2 UDM_Q05 message.

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        URD (URD): Results/update Definition, required
        URS (Optional[URS]): Unsolicited Selection, optional
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

    URD: _URD = Field(
        title="URD",
        description="Results/update Definition",
    )

    URS: Optional[_URS] = Field(
        default=None,
        title="URS",
        description="Unsolicited Selection",
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
