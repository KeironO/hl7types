"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: RDE_O11
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.RDE_O11_ORDER import RDE_O11_ORDER
from ..groups.RDE_O11_PATIENT import RDE_O11_PATIENT
from ..segments.MSH import MSH
from ..segments.NTE import NTE
from ..segments.SFT import SFT

_MSH = MSH
_NTE = NTE
_RDE_O11_ORDER = RDE_O11_ORDER
_RDE_O11_PATIENT = RDE_O11_PATIENT
_SFT = SFT


class RDE_O11(BaseModel):
    """HL7 v2 RDE_O11 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        NTE (Optional[List[NTE]]): optional
        PATIENT (Optional[RDE_O11_PATIENT]): optional
        ORDER (List[RDE_O11_ORDER]): required
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

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    PATIENT: _RDE_O11_PATIENT | None = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    ORDER: list[_RDE_O11_ORDER] = Field(
        default=...,
        title="ORDER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
