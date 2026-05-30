"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: CSU_C09.STUDY_PHASE
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.CSP import CSP

from .CSU_C09_STUDY_SCHEDULE import CSU_C09_STUDY_SCHEDULE

_CSP = CSP
_CSU_C09_STUDY_SCHEDULE = CSU_C09_STUDY_SCHEDULE


class CSU_C09_STUDY_PHASE(HL7Model):
    """HL7 v2 CSU_C09.STUDY_PHASE group.

    Attributes:
        CSP (Optional[CSP]): optional
        STUDY_SCHEDULE (List[CSU_C09_STUDY_SCHEDULE]): required
    """

    CSP: Optional[_CSP] = Field(
        default=None,
        title="CSP",
        description="Optional",
    )

    STUDY_SCHEDULE: List[_CSU_C09_STUDY_SCHEDULE] = Field(
        default=...,
        title="STUDY_SCHEDULE",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
