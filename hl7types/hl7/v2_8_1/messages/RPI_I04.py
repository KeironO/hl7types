"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: RPI_I04
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.RPI_I04_GUARANTOR_INSURANCE import RPI_I04_GUARANTOR_INSURANCE
from ..groups.RPI_I04_PROVIDER import RPI_I04_PROVIDER
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.NK1 import NK1
from ..segments.NTE import NTE
from ..segments.PID import PID
from ..segments.SFT import SFT
from ..segments.UAC import UAC

_MSA = MSA
_MSH = MSH
_NK1 = NK1
_NTE = NTE
_PID = PID
_RPI_I04_GUARANTOR_INSURANCE = RPI_I04_GUARANTOR_INSURANCE
_RPI_I04_PROVIDER = RPI_I04_PROVIDER
_SFT = SFT
_UAC = UAC


class RPI_I04(BaseModel):
    """HL7 v2 RPI_I04 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        MSA (MSA): required
        PROVIDER (List[RPI_I04_PROVIDER]): required
        PID (PID): required
        NK1 (Optional[List[NK1]]): optional
        GUARANTOR_INSURANCE (Optional[RPI_I04_GUARANTOR_INSURANCE]): optional
        NTE (Optional[List[NTE]]): optional
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

    UAC: _UAC | None = Field(
        default=None,
        title="UAC",
        description="Optional",
    )

    MSA: _MSA = Field(
        default=...,
        title="MSA",
        description="Required",
    )

    PROVIDER: list[_RPI_I04_PROVIDER] = Field(
        default=...,
        title="PROVIDER",
        description="Required, repeating",
    )

    PID: _PID = Field(
        default=...,
        title="PID",
        description="Required",
    )

    NK1: list[_NK1] | None = Field(
        default=None,
        title="NK1",
        description="Optional, repeating",
    )

    GUARANTOR_INSURANCE: _RPI_I04_GUARANTOR_INSURANCE | None = Field(
        default=None,
        title="GUARANTOR_INSURANCE",
        description="Optional",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
