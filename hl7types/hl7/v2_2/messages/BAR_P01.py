"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: BAR_P01
Type: Message
"""
from __future__ import annotations

from typing import List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.EVN import EVN
from ..segments.MSH import MSH
from ..segments.PID import PID

from ..groups.BAR_P01_VISIT import BAR_P01_VISIT

_BAR_P01_VISIT = BAR_P01_VISIT
_EVN = EVN
_MSH = MSH
_PID = PID


class BAR_P01(HL7Model):
    """HL7 v2 BAR_P01 message.

    Attributes:
        MSH (MSH): MESSAGE HEADER, required
        EVN (EVN): EVENT TYPE, required
        PID (PID): PATIENT IDENTIFICATION, required
        VISIT (List[BAR_P01_VISIT]): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="MESSAGE HEADER",
    )

    EVN: _EVN = Field(
        title="EVN",
        description="EVENT TYPE",
    )

    PID: _PID = Field(
        title="PID",
        description="PATIENT IDENTIFICATION",
    )

    VISIT: List[_BAR_P01_VISIT] = Field(
        min_length=1,
        title="VISIT",
    )

    model_config = {"populate_by_name": True}
