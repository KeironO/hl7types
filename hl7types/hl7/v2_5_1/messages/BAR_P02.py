"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: BAR_P02
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.EVN import EVN
from ..segments.MSH import MSH
from ..segments.SFT import SFT

from ..groups.BAR_P02_PATIENT import BAR_P02_PATIENT

_BAR_P02_PATIENT = BAR_P02_PATIENT
_EVN = EVN
_MSH = MSH
_SFT = SFT


class BAR_P02(HL7Model):
    """BAR/ACK - Purge patient accounts (S6.4.1).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        EVN (EVN): Event Type, required
        PATIENT (List[BAR_P02_PATIENT]): required
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

    EVN: _EVN = Field(
        title="EVN",
        description="Event Type",
    )

    PATIENT: List[_BAR_P02_PATIENT] = Field(
        min_length=1,
        title="PATIENT",
    )

    model_config = {"populate_by_name": True}
