"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: BAR_P01
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.EVN import EVN
from ..segments.MSH import MSH
from ..segments.PD1 import PD1
from ..segments.PID import PID

from ..groups.BAR_P01_VISIT import BAR_P01_VISIT

_BAR_P01_VISIT = BAR_P01_VISIT
_EVN = EVN
_MSH = MSH
_PD1 = PD1
_PID = PID


class BAR_P01(HL7Model):
    """BAR/ACK - Add patient accounts.

    Attributes:
        MSH (MSH): MSH - message header segment, required
        EVN (EVN): EVN - event type segment, required
        PID (PID): PID - patient identification segment, required
        PD1 (Optional[PD1]): PD1 - patient additional demographic segment, optional
        VISIT (List[BAR_P01_VISIT]): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="MSH - message header segment",
    )

    EVN: _EVN = Field(
        title="EVN",
        description="EVN - event type segment",
    )

    PID: _PID = Field(
        title="PID",
        description="PID - patient identification segment",
    )

    PD1: Optional[_PD1] = Field(
        default=None,
        title="PD1",
        description="PD1 - patient additional demographic segment",
    )

    VISIT: List[_BAR_P01_VISIT] = Field(
        min_length=1,
        title="VISIT",
    )

    model_config = {"populate_by_name": True}
