"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3.1
Class: ADT_A30
Type: Message
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.EVN import EVN
from ..segments.MRG import MRG
from ..segments.MSH import MSH
from ..segments.PD1 import PD1
from ..segments.PID import PID

_EVN = EVN
_MRG = MRG
_MSH = MSH
_PD1 = PD1
_PID = PID


class ADT_A30(HL7Model):
    """ADT/ACK -  Merge person information.

    Attributes:
        MSH (MSH): MSH - message header segment, required
        EVN (EVN): EVN - event type segment, required
        PID (PID): PID - patient identification segment, required
        PD1 (Optional[PD1]): PD1 - patient additional demographic segment, optional
        MRG (MRG): MRG - merge patient information segment-, required
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

    MRG: _MRG = Field(
        title="MRG",
        description="MRG - merge patient information segment-",
    )

    model_config = {"populate_by_name": True}
