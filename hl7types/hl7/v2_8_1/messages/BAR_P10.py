"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: BAR_P10
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.DG1 import DG1
from ..segments.EVN import EVN
from ..segments.GP1 import GP1
from ..segments.MSH import MSH
from ..segments.PID import PID
from ..segments.PV1 import PV1
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.BAR_P10_PROCEDURE import BAR_P10_PROCEDURE

_BAR_P10_PROCEDURE = BAR_P10_PROCEDURE
_DG1 = DG1
_EVN = EVN
_GP1 = GP1
_MSH = MSH
_PID = PID
_PV1 = PV1
_SFT = SFT
_UAC = UAC


class BAR_P10(HL7Model):
    """BAR/ACK -Transmit Ambulatory Payment  Classification(APC) (S6.4.1).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        EVN (EVN): Event Type, required
        PID (PID): Patient Identification, required
        PV1 (PV1): Patient Visit, required
        DG1 (Optional[List[DG1]]): Diagnosis, optional
        GP1 (GP1): Grouping/Reimbursement - Visit, required
        PROCEDURE (Optional[List[BAR_P10_PROCEDURE]]): optional
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

    PV1: _PV1 = Field(
        title="PV1",
        description="Patient Visit",
    )

    DG1: Optional[List[_DG1]] = Field(
        default=None,
        title="DG1",
        description="Diagnosis",
    )

    GP1: _GP1 = Field(
        title="GP1",
        description="Grouping/Reimbursement - Visit",
    )

    PROCEDURE: Optional[List[_BAR_P10_PROCEDURE]] = Field(
        default=None,
        title="PROCEDURE",
    )

    model_config = ConfigDict(populate_by_name=True)
