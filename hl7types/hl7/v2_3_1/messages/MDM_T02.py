"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: MDM_T02
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.EVN import EVN
from ..segments.MSH import MSH
from ..segments.OBX import OBX
from ..segments.PID import PID
from ..segments.PV1 import PV1
from ..segments.TXA import TXA

_EVN = EVN
_MSH = MSH
_OBX = OBX
_PID = PID
_PV1 = PV1
_TXA = TXA


class MDM_T02(BaseModel):
    """HL7 v2 MDM_T02 message.

    Attributes:
        MSH (MSH): required
        EVN (EVN): required
        PID (PID): required
        PV1 (PV1): required
        TXA (TXA): required
        OBX (List[OBX]): required
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

    OBX: list[_OBX] = Field(
        default=...,
        title="OBX",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
