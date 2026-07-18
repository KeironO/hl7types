"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: ADT_A30
Type: Message
"""
from __future__ import annotations

from typing import Optional
from pydantic import ConfigDict, Field
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
        MSH (MSH): Message header segment, required
        EVN (EVN): Event type, required
        PID (PID): Patient Identification, required
        PD1 (Optional[PD1]): Patient Demographic, optional
        MRG (MRG): Merge patient information, required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Message header segment",
    )

    EVN: _EVN = Field(
        title="EVN",
        description="Event type",
    )

    PID: _PID = Field(
        title="PID",
        description="Patient Identification",
    )

    PD1: Optional[_PD1] = Field(
        default=None,
        title="PD1",
        description="Patient Demographic",
    )

    MRG: _MRG = Field(
        title="MRG",
        description="Merge patient information",
    )

    model_config = ConfigDict(populate_by_name=True)
