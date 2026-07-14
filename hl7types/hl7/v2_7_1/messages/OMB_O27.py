"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: OMB_O27
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

from ..groups.OMB_O27_ORDER import OMB_O27_ORDER
from ..groups.OMB_O27_PATIENT import OMB_O27_PATIENT

_MSH = MSH
_NTE = NTE
_OMB_O27_ORDER = OMB_O27_ORDER
_OMB_O27_PATIENT = OMB_O27_PATIENT
_SFT = SFT
_UAC = UAC


class OMB_O27(HL7Model):
    """OMB - Blood product order (S4.12.1).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
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

    UAC: Optional[_UAC] = Field(
        default=None,
        title="UAC",
        description="User Authentication Credential Segment",
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

    model_config = {"populate_by_name": True}
