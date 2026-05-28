"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: CSU_C09.STUDY_PHASE
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.CSP import CSP
from .CSU_C09_STUDY_SCHEDULE import CSU_C09_STUDY_SCHEDULE

_CSP = CSP
_CSU_C09_STUDY_SCHEDULE = CSU_C09_STUDY_SCHEDULE


class CSU_C09_STUDY_PHASE(BaseModel):
    """HL7 v2 CSU_C09.STUDY_PHASE group.

    Attributes:
        CSP (Optional[List[CSP]]): optional
        STUDY_SCHEDULE (List[CSU_C09_STUDY_SCHEDULE]): required
    """

    CSP: list[_CSP] | None = Field(
        default=None,
        title="CSP",
        description="Optional, repeating",
    )

    STUDY_SCHEDULE: list[_CSU_C09_STUDY_SCHEDULE] = Field(
        default=...,
        title="STUDY_SCHEDULE",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
