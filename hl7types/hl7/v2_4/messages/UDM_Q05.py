"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
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
    """UDM/ACK - Unsolicited display update message (S5).

    Attributes:
        MSH (MSH): Message Header, required
        URD (URD): Results/update Definition, required
        URS (Optional[URS]): Unsolicited Selection, optional
        DSP (List[DSP]): Display Data, required
        DSC (Optional[DSC]): Continuation Pointer, optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message Header",
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

    model_config = {"populate_by_name": True}
