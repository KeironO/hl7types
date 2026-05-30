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
    """HL7 v2 UDM_Q05 message.

    Attributes:
        MSH (MSH): required
        URD (URD): required
        URS (Optional[URS]): optional
        DSP (List[DSP]): required
        DSC (Optional[DSC]): optional
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    URD: _URD = Field(
        default=...,
        title="URD",
        description="Required",
    )

    URS: Optional[_URS] = Field(
        default=None,
        title="URS",
        description="Optional",
    )

    DSP: List[_DSP] = Field(
        default=...,
        title="DSP",
        description="Required, repeating",
    )

    DSC: Optional[_DSC] = Field(
        default=None,
        title="DSC",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
