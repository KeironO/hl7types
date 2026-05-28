"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: RGV_O15
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.RGV_O15_ORDER import RGV_O15_ORDER
from ..groups.RGV_O15_PATIENT import RGV_O15_PATIENT
from ..segments.MSH import MSH
from ..segments.NTE import NTE
from ..segments.SFT import SFT
from ..segments.UAC import UAC

_MSH = MSH
_NTE = NTE
_RGV_O15_ORDER = RGV_O15_ORDER
_RGV_O15_PATIENT = RGV_O15_PATIENT
_SFT = SFT
_UAC = UAC


class RGV_O15(BaseModel):
    """HL7 v2 RGV_O15 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        NTE (Optional[List[NTE]]): optional
        PATIENT (Optional[RGV_O15_PATIENT]): optional
        ORDER (List[RGV_O15_ORDER]): required
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

    PATIENT: _RGV_O15_PATIENT | None = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    ORDER: list[_RGV_O15_ORDER] = Field(
        default=...,
        title="ORDER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
