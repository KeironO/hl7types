"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: ADT_A50
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
from ..segments.PV1 import PV1

_EVN = EVN
_MRG = MRG
_MSH = MSH
_PD1 = PD1
_PID = PID
_PV1 = PV1


class ADT_A50(HL7Model):
    """ADT/ACK - Change visit number (S3).

    Attributes:
        MSH (MSH): Message Header, required
        EVN (EVN): Event Type, required
        PID (PID): Patient identification, required
        PD1 (Optional[PD1]): patient additional demographic, optional
        MRG (MRG): Merge patient information, required
        PV1 (PV1): Patient visit, required
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

    MRG: _MRG = Field(
        title="MRG",
        description="Merge patient information",
    )

    PV1: _PV1 = Field(
        title="PV1",
        description="Patient visit",
    )

    model_config = {"populate_by_name": True}
