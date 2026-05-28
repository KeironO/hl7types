"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: ADT_A16
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.DG1 import DG1
from ..segments.EVN import EVN
from ..segments.MSH import MSH
from ..segments.PID import PID
from ..segments.PV1 import PV1

_DG1 = DG1
_EVN = EVN
_MSH = MSH
_PID = PID
_PV1 = PV1


class ADT_A16(BaseModel):
    """HL7 v2 ADT_A16 message.

    Attributes:
        MSH (MSH): required
        EVN (EVN): required
        PID (PID): required
        PV1 (PV1): required
        DG1 (Optional[DG1]): optional
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

    DG1: _DG1 | None = Field(
        default=None,
        title="DG1",
        description="Optional",
    )

    model_config = {"populate_by_name": True}
