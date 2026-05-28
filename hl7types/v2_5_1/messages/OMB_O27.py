"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: OMB_O27
Type: Message
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.MSH import MSH
from ..segments.NTE import NTE
from ..segments.SFT import SFT

from ..groups.OMB_O27_ORDER import OMB_O27_ORDER
from ..groups.OMB_O27_PATIENT import OMB_O27_PATIENT

_MSH = MSH
_NTE = NTE
_OMB_O27_ORDER = OMB_O27_ORDER
_OMB_O27_PATIENT = OMB_O27_PATIENT
_SFT = SFT


class OMB_O27(BaseModel):
    """HL7 v2 OMB_O27 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        NTE (Optional[List[NTE]]): optional
        PATIENT (Optional[OMB_O27_PATIENT]): optional
        ORDER (List[OMB_O27_ORDER]): required
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

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    PATIENT: Optional[_OMB_O27_PATIENT] = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    ORDER: List[_OMB_O27_ORDER] = Field(
        default=...,
        title="ORDER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
