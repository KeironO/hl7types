"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
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
from ..segments.UAC import UAC

from ..groups.BPS_O29_ORDER import BPS_O29_ORDER
from ..groups.BPS_O29_PATIENT import BPS_O29_PATIENT

_BPS_O29_ORDER = BPS_O29_ORDER
_BPS_O29_PATIENT = BPS_O29_PATIENT
_MSH = MSH
_NTE = NTE
_SFT = SFT
_UAC = UAC


class BPS_O29(HL7Model):
    """HL7 v2 BPS_O29 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        NTE (Optional[List[NTE]]): optional
        PATIENT (Optional[BPS_O29_PATIENT]): optional
        ORDER (List[BPS_O29_ORDER]): required
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

    PATIENT: Optional[_BPS_O29_PATIENT] = Field(
        default=None,
        title="PATIENT",
        description="Optional",
    )

    ORDER: List[_BPS_O29_ORDER] = Field(
        min_length=1,
        title="ORDER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
