"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: BAR_P10
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.DG1 import DG1
from ..segments.EVN import EVN
from ..segments.GP1 import GP1
from ..segments.MSH import MSH
from ..segments.PID import PID
from ..segments.PV1 import PV1
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.BAR_P10_PROCEDURE import BAR_P10_PROCEDURE

_BAR_P10_PROCEDURE = BAR_P10_PROCEDURE
_DG1 = DG1
_EVN = EVN
_GP1 = GP1
_MSH = MSH
_PID = PID
_PV1 = PV1
_SFT = SFT
_UAC = UAC


class BAR_P10(HL7Model):
    """HL7 v2 BAR_P10 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        EVN (EVN): required
        PID (PID): required
        PV1 (PV1): required
        DG1 (Optional[List[DG1]]): optional
        GP1 (GP1): required
        PROCEDURE (Optional[List[BAR_P10_PROCEDURE]]): optional
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

    UAC: Optional[_UAC] = Field(
        default=None,
        title="UAC",
        description="Optional",
    )

    EVN: _EVN = Field(
        default=...,
        title="EVN",
        description="Required",
    )

    PID: _PID = Field(
        default=...,
        title="PID",
        description="Required",
    )

    PV1: _PV1 = Field(
        default=...,
        title="PV1",
        description="Required",
    )

    DG1: Optional[List[_DG1]] = Field(
        default=None,
        title="DG1",
        description="Optional, repeating",
    )

    GP1: _GP1 = Field(
        default=...,
        title="GP1",
        description="Required",
    )

    PROCEDURE: Optional[List[_BAR_P10_PROCEDURE]] = Field(
        default=None,
        title="PROCEDURE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
