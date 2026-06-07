"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: PPT_PCL.PATIENT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.PID import PID

from .PPT_PCL_PATHWAY import PPT_PCL_PATHWAY
from .PPT_PCL_PATIENT_VISIT import PPT_PCL_PATIENT_VISIT

_PID = PID
_PPT_PCL_PATHWAY = PPT_PCL_PATHWAY
_PPT_PCL_PATIENT_VISIT = PPT_PCL_PATIENT_VISIT


class PPT_PCL_PATIENT(HL7Model):
    """HL7 v2 PPT_PCL.PATIENT group.

    Attributes:
        PID (PID): required
        PATIENT_VISIT (Optional[PPT_PCL_PATIENT_VISIT]): optional
        PATHWAY (List[PPT_PCL_PATHWAY]): required
    """

    PID: _PID = Field(
        title="PID",
        description="Required",
    )

    PATIENT_VISIT: Optional[_PPT_PCL_PATIENT_VISIT] = Field(
        default=None,
        title="PATIENT_VISIT",
        description="Optional",
    )

    PATHWAY: List[_PPT_PCL_PATHWAY] = Field(
        min_length=1,
        title="PATHWAY",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
