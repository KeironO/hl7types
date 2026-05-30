"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: PPR_PC1
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH
from ..segments.PID import PID

from ..groups.PPR_PC1_PATIENT_VISIT import PPR_PC1_PATIENT_VISIT
from ..groups.PPR_PC1_PROBLEM import PPR_PC1_PROBLEM

_MSH = MSH
_PID = PID
_PPR_PC1_PATIENT_VISIT = PPR_PC1_PATIENT_VISIT
_PPR_PC1_PROBLEM = PPR_PC1_PROBLEM


class PPR_PC1(HL7Model):
    """HL7 v2 PPR_PC1 message.

    Attributes:
        MSH (MSH): required
        PID (PID): required
        PATIENT_VISIT (Optional[PPR_PC1_PATIENT_VISIT]): optional
        PROBLEM (List[PPR_PC1_PROBLEM]): required
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    PID: _PID = Field(
        default=...,
        title="PID",
        description="Required",
    )

    PATIENT_VISIT: Optional[_PPR_PC1_PATIENT_VISIT] = Field(
        default=None,
        title="PATIENT_VISIT",
        description="Optional",
    )

    PROBLEM: List[_PPR_PC1_PROBLEM] = Field(
        default=...,
        title="PROBLEM",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
