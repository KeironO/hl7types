"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: UDM_Q05
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.DSC import DSC
from ..segments.DSP import DSP
from ..segments.MSH import MSH
from ..segments.URD import URD
from ..segments.URS import URS

_DSC = DSC
_DSP = DSP
_MSH = MSH
_URD = URD
_URS = URS


class UDM_Q05(HL7Model):
    """UDM/ACK - Unsolicited display update.

    Attributes:
        MSH (MSH): Message header segment, required
        URD (URD): Results/update definition segment, required
        URS (Optional[URS]): Unsolicited selection segment, optional
        DSP (List[DSP]): Display data segment, required
        DSC (Optional[DSC]): Continuation pointer segment, optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message header segment",
    )

    URD: _URD = Field(
        title="URD",
        description="Results/update definition segment",
    )

    URS: Optional[_URS] = Field(
        default=None,
        title="URS",
        description="Unsolicited selection segment",
    )

    DSP: List[_DSP] = Field(
        min_length=1,
        title="DSP",
        description="Display data segment",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="Continuation pointer segment",
    )

    model_config = {"populate_by_name": True}
