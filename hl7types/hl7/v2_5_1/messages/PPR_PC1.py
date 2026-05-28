"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: PPR_PC1
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.PPR_PC1_PATIENT_VISIT import PPR_PC1_PATIENT_VISIT
from ..groups.PPR_PC1_PROBLEM import PPR_PC1_PROBLEM
from ..segments.MSH import MSH
from ..segments.PID import PID
from ..segments.SFT import SFT

_MSH = MSH
_PID = PID
_PPR_PC1_PATIENT_VISIT = PPR_PC1_PATIENT_VISIT
_PPR_PC1_PROBLEM = PPR_PC1_PROBLEM
_SFT = SFT


class PPR_PC1(BaseModel):
    """HL7 v2 PPR_PC1 message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        PID (PID): required
        PATIENT_VISIT (Optional[PPR_PC1_PATIENT_VISIT]): optional
        PROBLEM (List[PPR_PC1_PROBLEM]): required
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    SFT: list[_SFT] | None = Field(
        default=None,
        title="SFT",
        description="Optional, repeating",
    )

    PID: _PID = Field(
        default=...,
        title="PID",
        description="Required",
    )

    PATIENT_VISIT: _PPR_PC1_PATIENT_VISIT | None = Field(
        default=None,
        title="PATIENT_VISIT",
        description="Optional",
    )

    PROBLEM: list[_PPR_PC1_PROBLEM] = Field(
        default=...,
        title="PROBLEM",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
