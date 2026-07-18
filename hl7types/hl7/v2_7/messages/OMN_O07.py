"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: OMN_O07
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

from ..groups.OMN_O07_ORDER import OMN_O07_ORDER
from ..groups.OMN_O07_PATIENT import OMN_O07_PATIENT

_MSH = MSH
_NTE = NTE
_OMN_O07_ORDER = OMN_O07_ORDER
_OMN_O07_PATIENT = OMN_O07_PATIENT
_SFT = SFT
_UAC = UAC


class OMN_O07(HL7Model):
    """OMN - Non-stock requisition order (S4.10.3).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        PATIENT (Optional[OMN_O07_PATIENT]): optional
        ORDER (List[OMN_O07_ORDER]): required
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

    PATIENT: Optional[_OMN_O07_PATIENT] = Field(
        default=None,
        title="PATIENT",
    )

    ORDER: List[_OMN_O07_ORDER] = Field(
        min_length=1,
        title="ORDER",
    )

    model_config = ConfigDict(populate_by_name=True)
