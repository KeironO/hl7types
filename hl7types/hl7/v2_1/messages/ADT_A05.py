"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.1
Class: ADT_A05
Type: Message
"""
from __future__ import annotations

from typing import Optional
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.DG1 import DG1
from ..segments.EVN import EVN
from ..segments.MSH import MSH
from ..segments.NK1 import NK1
from ..segments.PID import PID
from ..segments.PV1 import PV1

_DG1 = DG1
_EVN = EVN
_MSH = MSH
_NK1 = NK1
_PID = PID
_PV1 = PV1


class ADT_A05(HL7Model):
    """HL7 v2 ADT_A05 message.

    Attributes:
        MSH (MSH): MESSAGE HEADER, required
        EVN (EVN): EVENT TYPE, required
        PID (PID): PATIENT IDENTIFICATION, required
        NK1 (NK1): NEXT OF KIN, required
        PV1 (PV1): PATIENT VISIT, required
        DG1 (Optional[DG1]): DIAGNOSIS, optional
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

    NK1: _NK1 = Field(
        title="NK1",
        description="NEXT OF KIN",
    )

    PV1: _PV1 = Field(
        title="PV1",
        description="PATIENT VISIT",
    )

    DG1: Optional[_DG1] = Field(
        default=None,
        title="DG1",
        description="DIAGNOSIS",
    )

    model_config = ConfigDict(populate_by_name=True)
