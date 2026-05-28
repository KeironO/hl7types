"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: ADT_A30
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.EVN import EVN
from ..segments.MRG import MRG
from ..segments.MSH import MSH
from ..segments.PD1 import PD1
from ..segments.PID import PID
from ..segments.SFT import SFT

_EVN = EVN
_MRG = MRG
_MSH = MSH
_PD1 = PD1
_PID = PID
_SFT = SFT


class ADT_A30(BaseModel):
    """HL7 v2 ADT_A30 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        EVN (EVN): required
        PID (PID): required
        PD1 (Optional[PD1]): optional
        MRG (MRG): required
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    SFT: list[_SFT] | None = Field(
        default=None,
        title="SFT",
        description="Optional, repeating",
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

    PD1: _PD1 | None = Field(
        default=None,
        title="PD1",
        description="Optional",
    )

    MRG: _MRG = Field(
        default=...,
        title="MRG",
        description="Required",
    )

    model_config = {"populate_by_name": True}
