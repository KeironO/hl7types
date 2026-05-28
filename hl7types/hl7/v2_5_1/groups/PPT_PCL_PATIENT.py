"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: PPT_PCL.PATIENT
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.PID import PID
from .PPT_PCL_PATHWAY import PPT_PCL_PATHWAY
from .PPT_PCL_PATIENT_VISIT import PPT_PCL_PATIENT_VISIT

_PID = PID
_PPT_PCL_PATHWAY = PPT_PCL_PATHWAY
_PPT_PCL_PATIENT_VISIT = PPT_PCL_PATIENT_VISIT


class PPT_PCL_PATIENT(BaseModel):
    """HL7 v2 PPT_PCL.PATIENT group.

    Attributes:
        PID (PID): required
        PATIENT_VISIT (Optional[PPT_PCL_PATIENT_VISIT]): optional
        PATHWAY (List[PPT_PCL_PATHWAY]): required
    """

    PID: _PID = Field(
        default=...,
        title="PID",
        description="Required",
    )

    PATIENT_VISIT: _PPT_PCL_PATIENT_VISIT | None = Field(
        default=None,
        title="PATIENT_VISIT",
        description="Optional",
    )

    PATHWAY: list[_PPT_PCL_PATHWAY] = Field(
        default=...,
        title="PATHWAY",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
