"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: BAR_P02
Type: Message
"""
from __future__ import annotations

from typing import List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.EVN import EVN
from ..segments.MSH import MSH

from ..groups.BAR_P02_PATIENT import BAR_P02_PATIENT

_BAR_P02_PATIENT = BAR_P02_PATIENT
_EVN = EVN
_MSH = MSH


class BAR_P02(HL7Model):
    """BAR/ACK - Purge patient accounts (S6).

    Attributes:
        MSH (MSH): Message Header, required
        EVN (EVN): Event Type, required
        PATIENT (List[BAR_P02_PATIENT]): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message Header",
    )

    EVN: _EVN = Field(
        title="EVN",
        description="Event Type",
    )

    PATIENT: List[_BAR_P02_PATIENT] = Field(
        min_length=1,
        title="PATIENT",
    )

    model_config = ConfigDict(populate_by_name=True)
