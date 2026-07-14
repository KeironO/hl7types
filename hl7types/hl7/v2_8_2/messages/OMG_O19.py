"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: OMG_O19
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

from ..groups.OMG_O19_ORDER import OMG_O19_ORDER
from ..groups.OMG_O19_PATIENT import OMG_O19_PATIENT

_MSH = MSH
_NTE = NTE
_OMG_O19_ORDER = OMG_O19_ORDER
_OMG_O19_PATIENT = OMG_O19_PATIENT
_SFT = SFT
_UAC = UAC


class OMG_O19(HL7Model):
    """OMG - General clinical order (S4.4.4).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        PATIENT (Optional[OMG_O19_PATIENT]): optional
        ORDER (List[OMG_O19_ORDER]): required
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

    PATIENT: Optional[_OMG_O19_PATIENT] = Field(
        default=None,
        title="PATIENT",
    )

    ORDER: List[_OMG_O19_ORDER] = Field(
        min_length=1,
        title="ORDER",
    )

    model_config = {"populate_by_name": True}
