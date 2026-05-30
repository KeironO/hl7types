"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: RAS_O17
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

from ..groups.RAS_O17_ORDER import RAS_O17_ORDER
from ..groups.RAS_O17_PATIENT import RAS_O17_PATIENT

_MSH = MSH
_NTE = NTE
_RAS_O17_ORDER = RAS_O17_ORDER
_RAS_O17_PATIENT = RAS_O17_PATIENT
_SFT = SFT
_UAC = UAC


class RAS_O17(HL7Model):
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

    PATIENT: Optional[_RAS_O17_PATIENT] = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    ORDER: List[_RAS_O17_ORDER] = Field(
        default=...,
        title="ORDER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
