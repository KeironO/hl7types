"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: PPG_PCG
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH
from ..segments.PID import PID
from ..segments.SFT import SFT
from ..segments.UAC import UAC

from ..groups.PPG_PCG_PATHWAY import PPG_PCG_PATHWAY
from ..groups.PPG_PCG_PATIENT_VISIT import PPG_PCG_PATIENT_VISIT

_MSH = MSH
_PID = PID
_PPG_PCG_PATHWAY = PPG_PCG_PATHWAY
_PPG_PCG_PATIENT_VISIT = PPG_PCG_PATIENT_VISIT
_SFT = SFT
_UAC = UAC


class PPG_PCG(HL7Model):
    """HL7 v2 PPG_PCG message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        UAC (Optional[UAC]): optional
        PID (PID): required
        PATIENT_VISIT (Optional[PPG_PCG_PATIENT_VISIT]): optional
        PATHWAY (List[PPG_PCG_PATHWAY]): required
    """

    MSH: _MSH = Field(
        title="MSH",
        description="Required",
    )

    SFT: Optional[List[_SFT]] = Field(
        default=None,
        title="SFT",
        description="Optional, repeating",
    )

    UAC: Optional[_UAC] = Field(
        default=None,
        title="UAC",
        description="Optional",
    )

    PID: _PID = Field(
        title="PID",
        description="Required",
    )

    PATIENT_VISIT: Optional[_PPG_PCG_PATIENT_VISIT] = Field(
        default=None,
        title="PATIENT_VISIT",
        description="Optional",
    )

    PATHWAY: List[_PPG_PCG_PATHWAY] = Field(
        min_length=1,
        title="PATHWAY",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
