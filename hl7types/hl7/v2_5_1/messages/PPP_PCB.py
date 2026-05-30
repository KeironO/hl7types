"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: PPP_PCB
Type: Message
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.MSH import MSH
from ..segments.PID import PID
from ..segments.SFT import SFT

from ..groups.PPP_PCB_PATHWAY import PPP_PCB_PATHWAY
from ..groups.PPP_PCB_PATIENT_VISIT import PPP_PCB_PATIENT_VISIT

_MSH = MSH
_PID = PID
_PPP_PCB_PATHWAY = PPP_PCB_PATHWAY
_PPP_PCB_PATIENT_VISIT = PPP_PCB_PATIENT_VISIT
_SFT = SFT


class PPP_PCB(HL7Model):
    """HL7 v2 PPP_PCB message.

    Attributes:
        MSH (MSH): required
        SFT (Optional[List[SFT]]): optional
        PID (PID): required
        PATIENT_VISIT (Optional[PPP_PCB_PATIENT_VISIT]): optional
        PATHWAY (List[PPP_PCB_PATHWAY]): required
    """

    MSH: _MSH = Field(
        default=...,
        title="MSH",
        description="Required",
    )

    SFT: Optional[List[_SFT]] = Field(
        default=None,
        title="SFT",
        description="Optional, repeating",
    )

    PID: _PID = Field(
        default=...,
        title="PID",
        description="Required",
    )

    PATIENT_VISIT: Optional[_PPP_PCB_PATIENT_VISIT] = Field(
        default=None,
        title="PATIENT_VISIT",
        description="Optional",
    )

    PATHWAY: List[_PPP_PCB_PATHWAY] = Field(
        default=...,
        title="PATHWAY",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
