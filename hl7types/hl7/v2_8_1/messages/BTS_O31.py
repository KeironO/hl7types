"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: BTS_O31
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.BTS_O31_ORDER import BTS_O31_ORDER
from ..groups.BTS_O31_PATIENT import BTS_O31_PATIENT
from ..segments.MSH import MSH
from ..segments.NTE import NTE
from ..segments.SFT import SFT
from ..segments.UAC import UAC

_BTS_O31_ORDER = BTS_O31_ORDER
_BTS_O31_PATIENT = BTS_O31_PATIENT
_MSH = MSH
_NTE = NTE
_SFT = SFT
_UAC = UAC


class BTS_O31(BaseModel):
    """HL7 v2 BTS_O31 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        NTE (Optional[List[NTE]]): optional
        PATIENT (Optional[BTS_O31_PATIENT]): optional
        ORDER (List[BTS_O31_ORDER]): required
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

    PATIENT: _BTS_O31_PATIENT | None = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    ORDER: list[_BTS_O31_ORDER] = Field(
        default=...,
        title="ORDER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
