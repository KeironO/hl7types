"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: OMQ_O57
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

from ..groups.OMQ_O57_ORDER import OMQ_O57_ORDER
from ..groups.OMQ_O57_PATIENT import OMQ_O57_PATIENT

_MSH = MSH
_NTE = NTE
_OMQ_O57_ORDER = OMQ_O57_ORDER
_OMQ_O57_PATIENT = OMQ_O57_PATIENT
_SFT = SFT
_UAC = UAC


class OMQ_O57(HL7Model):
    """HL7 v2 OMQ_O57 message.

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        PATIENT (Optional[OMQ_O57_PATIENT]): optional
        ORDER (List[OMQ_O57_ORDER]): required
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

    PATIENT: Optional[_OMQ_O57_PATIENT] = Field(
        default=None,
        title="PATIENT",
    )

    ORDER: List[_OMQ_O57_ORDER] = Field(
        min_length=1,
        title="ORDER",
    )

    model_config = {"populate_by_name": True}
