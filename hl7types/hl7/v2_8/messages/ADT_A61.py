"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: ADT_A61
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
from ..segments.PV1 import PV1
from ..segments.PV2 import PV2
from ..segments.ROL import ROL
from ..segments.SFT import SFT
from ..segments.UAC import UAC

_EVN = EVN
_MSH = MSH
_PD1 = PD1
_PID = PID
_PV1 = PV1
_PV2 = PV2
_ROL = ROL
_SFT = SFT
_UAC = UAC


class ADT_A61(HL7Model):
    """ADT/ACK - Change consulting doctor (S3.3.1).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        EVN (EVN): Event Type, required
        PID (PID): Patient Identification, required
        PD1 (Optional[PD1]): Patient Additional Demographic, optional
        ROL (Optional[List[ROL]]): Role, optional
        PV1 (PV1): Patient Visit, required
        PV2 (Optional[PV2]): Patient Visit - Additional Information, optional
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

    UAC: Optional[_UAC] = Field(
        default=None,
        title="UAC",
        description="User Authentication Credential Segment",
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

    PV1: _PV1 = Field(
        title="PV1",
        description="Patient Visit",
    )

    PV2: Optional[_PV2] = Field(
        default=None,
        title="PV2",
        description="Patient Visit - Additional Information",
    )

    model_config = {"populate_by_name": True}
