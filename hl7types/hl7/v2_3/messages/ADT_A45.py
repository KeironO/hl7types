"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: ADT_A45
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

from ..groups.ADT_A45_MERGE_INFO import ADT_A45_MERGE_INFO

_ADT_A45_MERGE_INFO = ADT_A45_MERGE_INFO
_EVN = EVN
_MSH = MSH
_PD1 = PD1
_PID = PID


class ADT_A45(HL7Model):
    """ADT/ACK - Move visit information - visit number.

    Attributes:
        MSH (MSH): Message header segment, required
        EVN (EVN): Event type, required
        PID (PID): Patient Identification, required
        PD1 (Optional[PD1]): Patient Demographic, optional
        MERGE_INFO (List[ADT_A45_MERGE_INFO]): required
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

    MERGE_INFO: List[_ADT_A45_MERGE_INFO] = Field(
        min_length=1,
        title="MERGE_INFO",
    )

    model_config = {"populate_by_name": True}
