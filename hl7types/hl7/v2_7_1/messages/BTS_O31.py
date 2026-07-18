"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: BTS_O31
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH
from ..segments.NTE import NTE
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.BTS_O31_ORDER import BTS_O31_ORDER
from ..groups.BTS_O31_PATIENT import BTS_O31_PATIENT

_BTS_O31_ORDER = BTS_O31_ORDER
_BTS_O31_PATIENT = BTS_O31_PATIENT
_MSH = MSH
_NTE = NTE
_SFT = SFT
_UAC = UAC


class BTS_O31(HL7Model):
    """BTS - Blood product transfusion/disposition (S4.12.5).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        PATIENT (Optional[BTS_O31_PATIENT]): optional
        ORDER (List[BTS_O31_ORDER]): required
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

    PATIENT: Optional[_BTS_O31_PATIENT] = Field(
        default=None,
        title="PATIENT",
    )

    ORDER: List[_BTS_O31_ORDER] = Field(
        min_length=1,
        title="ORDER",
    )

    model_config = ConfigDict(populate_by_name=True)
