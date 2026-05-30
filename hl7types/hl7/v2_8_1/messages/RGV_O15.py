"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: RGV_O15
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH
from ..segments.NTE import NTE
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.RGV_O15_ORDER import RGV_O15_ORDER
from ..groups.RGV_O15_PATIENT import RGV_O15_PATIENT

_MSH = MSH
_NTE = NTE
_RGV_O15_ORDER = RGV_O15_ORDER
_RGV_O15_PATIENT = RGV_O15_PATIENT
_SFT = SFT
_UAC = UAC


class RGV_O15(HL7Model):
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

    PATIENT: Optional[_RGV_O15_PATIENT] = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    ORDER: List[_RGV_O15_ORDER] = Field(
        default=...,
        title="ORDER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
