"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: RQP_I04
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.RQP_I04_PROVIDER import RQP_I04_PROVIDER
from ..segments.GT1 import GT1
from ..segments.MSH import MSH
from ..segments.NK1 import NK1
from ..segments.NTE import NTE
from ..segments.PID import PID
from ..segments.SFT import SFT
from ..segments.UAC import UAC

_GT1 = GT1
_MSH = MSH
_NK1 = NK1
_NTE = NTE
_PID = PID
_RQP_I04_PROVIDER = RQP_I04_PROVIDER
_SFT = SFT
_UAC = UAC


class RQP_I04(BaseModel):
    """HL7 v2 RQP_I04 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        PROVIDER (List[RQP_I04_PROVIDER]): required
        PID (PID): required
        NK1 (Optional[List[NK1]]): optional
        GT1 (Optional[List[GT1]]): optional
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

    PROVIDER: list[_RQP_I04_PROVIDER] = Field(
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

    GT1: list[_GT1] | None = Field(
        default=None,
        title="GT1",
        description="Optional, repeating",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
