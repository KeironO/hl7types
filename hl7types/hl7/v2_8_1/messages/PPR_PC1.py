"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: PPR_PC1
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH
from ..segments.PID import PID
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.PPR_PC1_PATIENT_VISIT import PPR_PC1_PATIENT_VISIT
from ..groups.PPR_PC1_PROBLEM import PPR_PC1_PROBLEM

_MSH = MSH
_PID = PID
_PPR_PC1_PATIENT_VISIT = PPR_PC1_PATIENT_VISIT
_PPR_PC1_PROBLEM = PPR_PC1_PROBLEM
_SFT = SFT
_UAC = UAC


class PPR_PC1(HL7Model):
    """PPR - PC/ problem add (S12.3.2).

    Attributes:
        MSH (MSH): Message Header, required
        SFT (Optional[List[SFT]]): Software Segment, optional
        UAC (Optional[UAC]): User Authentication Credential Segment, optional
        PID (PID): Patient Identification, required
        PATIENT_VISIT (Optional[PPR_PC1_PATIENT_VISIT]): optional
        PROBLEM (List[PPR_PC1_PROBLEM]): required
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

    PID: _PID = Field(
        title="PID",
        description="Patient Identification",
    )

    PATIENT_VISIT: Optional[_PPR_PC1_PATIENT_VISIT] = Field(
        default=None,
        title="PATIENT_VISIT",
    )

    PROBLEM: List[_PPR_PC1_PROBLEM] = Field(
        min_length=1,
        title="PROBLEM",
    )

    model_config = ConfigDict(populate_by_name=True)
