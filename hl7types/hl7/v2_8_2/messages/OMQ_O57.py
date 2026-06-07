"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
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
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        NTE (Optional[List[NTE]]): optional
        PATIENT (Optional[OMQ_O57_PATIENT]): optional
        ORDER (List[OMQ_O57_ORDER]): required
    """

    MSH: _MSH = Field(
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

    PATIENT: Optional[_OMQ_O57_PATIENT] = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    ORDER: List[_OMQ_O57_ORDER] = Field(
        min_length=1,
        title="ORDER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
