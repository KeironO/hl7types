"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: BAR_P12
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.DG1 import DG1
from ..segments.DRG import DRG
from ..segments.EVN import EVN
from ..segments.MSH import MSH
from ..segments.PID import PID
from ..segments.PV1 import PV1
from ..segments.SFT import SFT

from ..groups.BAR_P12_PROCEDURE import BAR_P12_PROCEDURE

_BAR_P12_PROCEDURE = BAR_P12_PROCEDURE
_DG1 = DG1
_DRG = DRG
_EVN = EVN
_MSH = MSH
_PID = PID
_PV1 = PV1
_SFT = SFT


class BAR_P12(HL7Model):
    """HL7 v2 BAR_P12 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        EVN (EVN): required
        PID (PID): required
        PV1 (PV1): required
        DG1 (Optional[List[DG1]]): optional
        DRG (Optional[DRG]): optional
        PROCEDURE (Optional[List[BAR_P12_PROCEDURE]]): optional
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Required",
    )

    SFT: Optional[List[_SFT]] = Field(
        default=None,
        title="SFT",
        description="Optional, repeating",
    )

    EVN: _EVN = Field(
        title="EVN",
        description="Required",
    )

    PID: _PID = Field(
        title="PID",
        description="Required",
    )

    PV1: _PV1 = Field(
        title="PV1",
        description="Required",
    )

    DG1: Optional[List[_DG1]] = Field(
        default=None,
        title="DG1",
        description="Optional, repeating",
    )

    DRG: Optional[_DRG] = Field(
        default=None,
        title="DRG",
        description="Optional",
    )

    PROCEDURE: Optional[List[_BAR_P12_PROCEDURE]] = Field(
        default=None,
        title="PROCEDURE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
