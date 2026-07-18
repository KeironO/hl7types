"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: RAS_O17
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

from ..groups.RAS_O17_ORDER import RAS_O17_ORDER
from ..groups.RAS_O17_PATIENT import RAS_O17_PATIENT

_MSH = MSH
_NTE = NTE
_RAS_O17_ORDER = RAS_O17_ORDER
_RAS_O17_PATIENT = RAS_O17_PATIENT
_SFT = SFT
_UAC = UAC


class RAS_O17(HL7Model):
    """RAS - Pharmacy/treatment administration (S4.A.11).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        PATIENT (Optional[RAS_O17_PATIENT]): optional
        ORDER (List[RAS_O17_ORDER]): required
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

    PATIENT: Optional[_RAS_O17_PATIENT] = Field(
        default=None,
        title="PATIENT",
    )

    ORDER: List[_RAS_O17_ORDER] = Field(
        min_length=1,
        title="ORDER",
    )

    model_config = ConfigDict(populate_by_name=True)
