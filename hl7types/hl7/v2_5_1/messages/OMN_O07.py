"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: OMN_O07
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.OMN_O07_ORDER import OMN_O07_ORDER
from ..groups.OMN_O07_PATIENT import OMN_O07_PATIENT
from ..segments.MSH import MSH
from ..segments.NTE import NTE
from ..segments.SFT import SFT

_MSH = MSH
_NTE = NTE
_OMN_O07_ORDER = OMN_O07_ORDER
_OMN_O07_PATIENT = OMN_O07_PATIENT
_SFT = SFT


class OMN_O07(BaseModel):
    """HL7 v2 OMN_O07 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        NTE (Optional[List[NTE]]): optional
        PATIENT (Optional[OMN_O07_PATIENT]): optional
        ORDER (List[OMN_O07_ORDER]): required
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

    PATIENT: _OMN_O07_PATIENT | None = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    ORDER: list[_OMN_O07_ORDER] = Field(
        default=...,
        title="ORDER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
