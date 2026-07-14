"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: BAR_P05
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
from ..segments.ROL import ROL

from ..groups.BAR_P05_VISIT import BAR_P05_VISIT

_BAR_P05_VISIT = BAR_P05_VISIT
_EVN = EVN
_MSH = MSH
_PD1 = PD1
_PID = PID
_ROL = ROL


class BAR_P05(HL7Model):
    """BAR/ACK - Update account (S6).

    Attributes:
        MSH (MSH): Message Header, required
        EVN (EVN): Event Type, required
        PID (PID): Patient identification, required
        PD1 (Optional[PD1]): patient additional demographic, optional
        ROL (Optional[List[ROL]]): Role, optional
        VISIT (List[BAR_P05_VISIT]): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message Header",
    )

    EVN: _EVN = Field(
        title="EVN",
        description="Event Type",
    )

    PID: _PID = Field(
        title="PID",
        description="Patient identification",
    )

    PD1: Optional[_PD1] = Field(
        default=None,
        title="PD1",
        description="patient additional demographic",
    )

    ROL: Optional[List[_ROL]] = Field(
        default=None,
        title="ROL",
        description="Role",
    )

    VISIT: List[_BAR_P05_VISIT] = Field(
        min_length=1,
        title="VISIT",
    )

    model_config = {"populate_by_name": True}
