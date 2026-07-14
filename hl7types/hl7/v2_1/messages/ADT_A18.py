"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: ADT_A18
Type: Message
"""
from __future__ import annotations

from typing import Optional
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.EVN import EVN
from ..segments.MRG import MRG
from ..segments.MSH import MSH
from ..segments.PID import PID
from ..segments.PV1 import PV1

_EVN = EVN
_MRG = MRG
_MSH = MSH
_PID = PID
_PV1 = PV1


class ADT_A18(HL7Model):
    """HL7 v2 ADT_A18 message.

    Attributes:
        MSH (MSH): MESSAGE HEADER, required
        EVN (EVN): EVENT TYPE, required
        PID (PID): PATIENT IDENTIFICATION, required
        MRG (MRG): MERGE PATIENT INFORMATION, required
        PV1 (Optional[PV1]): PATIENT VISIT, optional
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

    MRG: _MRG = Field(
        title="MRG",
        description="MERGE PATIENT INFORMATION",
    )

    PV1: Optional[_PV1] = Field(
        default=None,
        title="PV1",
        description="PATIENT VISIT",
    )

    model_config = {"populate_by_name": True}
