"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: OMB_O27
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

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


class OMB_O27(HL7Model):
    """OMB - Blood product order (S4.20.1).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        PATIENT (Optional[OMB_O27_PATIENT]): optional
        ORDER (List[OMB_O27_ORDER]): required
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

    PATIENT: Optional[_OMB_O27_PATIENT] = Field(
        default=None,
        title="PATIENT",
    )

    ORDER: List[_OMB_O27_ORDER] = Field(
        min_length=1,
        title="ORDER",
    )

    model_config = ConfigDict(populate_by_name=True)
