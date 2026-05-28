"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: OMN_O07
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.MSH import MSH
from ..segments.NTE import NTE
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.OMN_O07_ORDER import OMN_O07_ORDER
from ..groups.OMN_O07_PATIENT import OMN_O07_PATIENT

_MSH = MSH
_NTE = NTE
_OMN_O07_ORDER = OMN_O07_ORDER
_OMN_O07_PATIENT = OMN_O07_PATIENT
_SFT = SFT
_UAC = UAC


class OMN_O07(BaseModel):
    """HL7 v2 OMN_O07 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        NTE (Optional[List[NTE]]): optional
        PATIENT (Optional[OMN_O07_PATIENT]): optional
        ORDER (List[OMN_O07_ORDER]): required
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    SFT: Optional[List[_SFT]] = Field(
        default=None,
        title="SFT",
        description="Optional, repeating",
    )

    UAC: Optional[_UAC] = Field(
        default=None,
        title="UAC",
        description="Optional",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    PATIENT: Optional[_OMN_O07_PATIENT] = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    ORDER: List[_OMN_O07_ORDER] = Field(
        default=...,
        title="ORDER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
