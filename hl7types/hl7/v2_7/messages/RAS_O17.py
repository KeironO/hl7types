"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: RAS_O17
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.RAS_O17_ORDER import RAS_O17_ORDER
from ..groups.RAS_O17_PATIENT import RAS_O17_PATIENT
from ..segments.MSH import MSH
from ..segments.NTE import NTE
from ..segments.SFT import SFT
from ..segments.UAC import UAC

_MSH = MSH
_NTE = NTE
_RAS_O17_ORDER = RAS_O17_ORDER
_RAS_O17_PATIENT = RAS_O17_PATIENT
_SFT = SFT
_UAC = UAC


class RAS_O17(BaseModel):
    """HL7 v2 RAS_O17 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        NTE (Optional[List[NTE]]): optional
        PATIENT (Optional[RAS_O17_PATIENT]): optional
        ORDER (List[RAS_O17_ORDER]): required
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

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    PATIENT: _RAS_O17_PATIENT | None = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    ORDER: list[_RAS_O17_ORDER] = Field(
        default=...,
        title="ORDER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
