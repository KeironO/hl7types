"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: RPI_I01
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.RPI_I01_GUARANTOR_INSURANCE import RPI_I01_GUARANTOR_INSURANCE
from ..groups.RPI_I01_PROVIDER import RPI_I01_PROVIDER
from ..segments.MSA import MSA
from ..segments.MSH import MSH
from ..segments.NK1 import NK1
from ..segments.NTE import NTE
from ..segments.PID import PID

_MSA = MSA
_MSH = MSH
_NK1 = NK1
_NTE = NTE
_PID = PID
_RPI_I01_GUARANTOR_INSURANCE = RPI_I01_GUARANTOR_INSURANCE
_RPI_I01_PROVIDER = RPI_I01_PROVIDER


class RPI_I01(BaseModel):
    """HL7 v2 RPI_I01 message.

    Attributes:
        MSH (MSH): required
        MSA (MSA): required
        PROVIDER (List[RPI_I01_PROVIDER]): required
        PID (PID): required
        NK1 (Optional[List[NK1]]): optional
        GUARANTOR_INSURANCE (Optional[RPI_I01_GUARANTOR_INSURANCE]): optional
        NTE (Optional[List[NTE]]): optional
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    MSA: _MSA = Field(
        default=...,
        title="MSA",
        description="Required",
    )

    PROVIDER: list[_RPI_I01_PROVIDER] = Field(
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

    GUARANTOR_INSURANCE: _RPI_I01_GUARANTOR_INSURANCE | None = Field(
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
