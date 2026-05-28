"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: ADT_A18
Type: Message
"""
from __future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field

from ..segments.EVN import EVN
from ..segments.MRG import MRG
from ..segments.MSH import MSH
from ..segments.PID import PID
from ..segments.PV1 import PV1

_EVN = EVN
_MRG = MRG
_MSH = MSH
_PID = PID
_PV1 = PV1


class ADT_A18(BaseModel):
    """HL7 v2 ADT_A18 message.

    Attributes:
        MSH (MSH): required
        EVN (EVN): required
        PID (PID): required
        MRG (MRG): required
        PV1 (Optional[PV1]): optional
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
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

    MRG: _MRG = Field(
        default=...,
        title="MRG",
        description="Required",
    )

    PV1: Optional[_PV1] = Field(
        default=None,
        title="PV1",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
