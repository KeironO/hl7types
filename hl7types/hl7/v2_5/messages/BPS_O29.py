"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: BPS_O29
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH
from ..segments.NTE import NTE
from ..segments.SFT import SFT

from ..groups.BPS_O29_ORDER import BPS_O29_ORDER
from ..groups.BPS_O29_PATIENT import BPS_O29_PATIENT

_BPS_O29_ORDER = BPS_O29_ORDER
_BPS_O29_PATIENT = BPS_O29_PATIENT
_MSH = MSH
_NTE = NTE
_SFT = SFT


class BPS_O29(HL7Model):
    """BPS - Blood product dispense status (S4.20.3).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        PATIENT (Optional[BPS_O29_PATIENT]): optional
        ORDER (List[BPS_O29_ORDER]): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message Header",
    )

    SFT: Optional[List[_SFT]] = Field(
        default=None,
        title="SFT",
        description="Software Segment",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    PATIENT: Optional[_BPS_O29_PATIENT] = Field(
        default=None,
        title="PATIENT",
    )

    ORDER: List[_BPS_O29_ORDER] = Field(
        min_length=1,
        title="ORDER",
    )

    model_config = {"populate_by_name": True}
