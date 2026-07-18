"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: ADT_A24
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.DB1 import DB1
from ..segments.EVN import EVN
from ..segments.MSH import MSH
from ..segments.PD1 import PD1
from ..segments.PID import PID
from ..segments.PV1 import PV1

_DB1 = DB1
_EVN = EVN
_MSH = MSH
_PD1 = PD1
_PID = PID
_PV1 = PV1


class ADT_A24(HL7Model):
    """ADT/ACK -  Link patient information (S3).

    Attributes:
        MSH (MSH): Message Header, required
        EVN (EVN): Event Type, required
        PID (PID): Patient identification, required
        PD1 (Optional[PD1]): patient additional demographic, optional
        PV1 (Optional[PV1]): Patient visit, optional
        DB1 (Optional[List[DB1]]): Disability, optional
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

    PV1: Optional[_PV1] = Field(
        default=None,
        title="PV1",
        description="Patient visit",
    )

    DB1: Optional[List[_DB1]] = Field(
        default=None,
        title="DB1",
        description="Disability",
    )

    model_config = ConfigDict(populate_by_name=True)
