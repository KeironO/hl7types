"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: BAR_P01
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.EVN import EVN
from ..segments.MSH import MSH
from ..segments.PD1 import PD1
from ..segments.PID import PID
from ..segments.ROL import ROL
from ..segments.SFT import SFT

from ..groups.BAR_P01_VISIT import BAR_P01_VISIT

_BAR_P01_VISIT = BAR_P01_VISIT
_EVN = EVN
_MSH = MSH
_PD1 = PD1
_PID = PID
_ROL = ROL
_SFT = SFT


class BAR_P01(HL7Model):
    """BAR/ACK - Add patient accounts (S6.4.1).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        EVN (EVN): Event Type, required
        PID (PID): Patient Identification, required
        PD1 (Optional[PD1]): Patient Additional Demographic, optional
        ROL (Optional[List[ROL]]): Role, optional
        VISIT (List[BAR_P01_VISIT]): required
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

    PID: _PID = Field(
        title="PID",
        description="Patient Identification",
    )

    PD1: Optional[_PD1] = Field(
        default=None,
        title="PD1",
        description="Patient Additional Demographic",
    )

    ROL: Optional[List[_ROL]] = Field(
        default=None,
        title="ROL",
        description="Role",
    )

    VISIT: List[_BAR_P01_VISIT] = Field(
        min_length=1,
        title="VISIT",
    )

    model_config = ConfigDict(populate_by_name=True)
