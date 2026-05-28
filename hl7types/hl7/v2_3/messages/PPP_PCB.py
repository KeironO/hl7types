"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: PPP_PCB
Type: Message
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..groups.PPP_PCB_PATHWAY import PPP_PCB_PATHWAY
from ..groups.PPP_PCB_PATIENT_VISIT import PPP_PCB_PATIENT_VISIT
from ..segments.MSH import MSH
from ..segments.PID import PID

_MSH = MSH
_PID = PID
_PPP_PCB_PATHWAY = PPP_PCB_PATHWAY
_PPP_PCB_PATIENT_VISIT = PPP_PCB_PATIENT_VISIT


class PPP_PCB(BaseModel):
    """HL7 v2 PPP_PCB message.

    Attributes:
        MSH (MSH): required
        PID (PID): required
        PATIENT_VISIT (Optional[PPP_PCB_PATIENT_VISIT]): optional
        PATHWAY (List[PPP_PCB_PATHWAY]): required
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

    PATIENT_VISIT: _PPP_PCB_PATIENT_VISIT | None = Field(
        default=None,
        title="PATIENT_VISIT",
        description="Optional",
    )

    PATHWAY: list[_PPP_PCB_PATHWAY] = Field(
        default=...,
        title="PATHWAY",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
