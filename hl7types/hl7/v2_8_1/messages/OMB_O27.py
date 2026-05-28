"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: OMB_O27
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.OMB_O27_ORDER import OMB_O27_ORDER
from ..groups.OMB_O27_PATIENT import OMB_O27_PATIENT
from ..segments.MSH import MSH
from ..segments.NTE import NTE
from ..segments.SFT import SFT
from ..segments.UAC import UAC

_MSH = MSH
_NTE = NTE
_OMB_O27_ORDER = OMB_O27_ORDER
_OMB_O27_PATIENT = OMB_O27_PATIENT
_SFT = SFT
_UAC = UAC


class OMB_O27(BaseModel):
    """HL7 v2 OMB_O27 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        NTE (Optional[List[NTE]]): optional
        PATIENT (Optional[OMB_O27_PATIENT]): optional
        ORDER (List[OMB_O27_ORDER]): required
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

    PATIENT: _OMB_O27_PATIENT | None = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    ORDER: list[_OMB_O27_ORDER] = Field(
        default=...,
        title="ORDER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
