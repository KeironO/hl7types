"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: RGV_O15
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

from ..groups.RGV_O15_ORDER import RGV_O15_ORDER
from ..groups.RGV_O15_PATIENT import RGV_O15_PATIENT

_MSH = MSH
_NTE = NTE
_RGV_O15_ORDER = RGV_O15_ORDER
_RGV_O15_PATIENT = RGV_O15_PATIENT
_SFT = SFT
_UAC = UAC


class RGV_O15(HL7Model):
    """RGV - Pharmacy/treatment give (S4.A.3.8).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        PATIENT (Optional[RGV_O15_PATIENT]): optional
        ORDER (List[RGV_O15_ORDER]): required
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

    PATIENT: Optional[_RGV_O15_PATIENT] = Field(
        default=None,
        title="PATIENT",
    )

    ORDER: List[_RGV_O15_ORDER] = Field(
        min_length=1,
        title="ORDER",
    )

    model_config = ConfigDict(populate_by_name=True)
