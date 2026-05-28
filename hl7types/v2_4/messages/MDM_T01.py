"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: MDM_T01
Type: Message
"""
from _future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field

from ..segments.EVN import EVN
from ..segments.MSH import MSH
from ..segments.PID import PID
from ..segments.PV1 import PV1
from ..segments.TXA import TXA

_EVN = EVN
_MSH = MSH
_PID = PID
_PV1 = PV1
_TXA = TXA


class MDM_T01(BaseModel):
    """HL7 v2 MDM_T01 message.

    Attributes:
        MSH (MSH): required
        EVN (EVN): required
        PID (PID): required
        PV1 (PV1): required
        TXA (TXA): required
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

    PV1: _PV1 = Field(
        default=...,
        title="PV1",
        description="Required",
    )

    TXA: _TXA = Field(
        default=...,
        title="TXA",
        description="Required",
    )

    model_config = {"populate_by_name": True}
