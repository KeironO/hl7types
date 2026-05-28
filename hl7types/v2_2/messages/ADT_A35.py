"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: ADT_A35
Type: Message
"""
from _future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field

from ..segments.EVN import EVN
from ..segments.MRG import MRG
from ..segments.MSH import MSH
from ..segments.PID import PID

_EVN = EVN
_MRG = MRG
_MSH = MSH
_PID = PID


class ADT_A35(BaseModel):
    """HL7 v2 ADT_A35 message.

    Attributes:
        MSH (MSH): required
        EVN (EVN): required
        PID (PID): required
        MRG (MRG): required
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

    model_config = {"populate_by_name": True}
