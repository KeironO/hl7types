"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: PPV_PCA.PATIENT
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.PID import PID

from .PPV_PCA_GOAL import PPV_PCA_GOAL
from .PPV_PCA_PATIENT_VISIT import PPV_PCA_PATIENT_VISIT

_PID = PID
_PPV_PCA_GOAL = PPV_PCA_GOAL
_PPV_PCA_PATIENT_VISIT = PPV_PCA_PATIENT_VISIT


class PPV_PCA_PATIENT(HL7Model):
    """HL7 v2 PPV_PCA.PATIENT group.

    Attributes:
        PID (PID): required
        PATIENT_VISIT (Optional[PPV_PCA_PATIENT_VISIT]): optional
        GOAL (List[PPV_PCA_GOAL]): required
    """

    PID: _PID = Field(
        default=...,
        title="PID",
        description="Required",
    )

    PATIENT_VISIT: Optional[_PPV_PCA_PATIENT_VISIT] = Field(
        default=None,
        title="PATIENT_VISIT",
        description="Optional",
    )

    GOAL: List[_PPV_PCA_GOAL] = Field(
        default=...,
        title="GOAL",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
