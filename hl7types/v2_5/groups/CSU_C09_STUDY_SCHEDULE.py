"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: CSU_C09.STUDY_SCHEDULE
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.CSS import CSS

from .CSU_C09_STUDY_OBSERVATION import CSU_C09_STUDY_OBSERVATION
from .CSU_C09_STUDY_PHARM import CSU_C09_STUDY_PHARM

_CSS = CSS
_CSU_C09_STUDY_OBSERVATION = CSU_C09_STUDY_OBSERVATION
_CSU_C09_STUDY_PHARM = CSU_C09_STUDY_PHARM


class CSU_C09_STUDY_SCHEDULE(BaseModel):
    """HL7 v2 CSU_C09.STUDY_SCHEDULE group.

    Attributes:
        CSS (Optional[CSS]): optional
        STUDY_OBSERVATION (List[CSU_C09_STUDY_OBSERVATION]): required
        STUDY_PHARM (List[CSU_C09_STUDY_PHARM]): required
    """

    CSS: Optional[_CSS] = Field(
        default=None,
        title="CSS",
        description="Optional",
    )

    STUDY_OBSERVATION: List[_CSU_C09_STUDY_OBSERVATION] = Field(
        default=...,
        title="STUDY_OBSERVATION",
        description="Required, repeating",
    )

    STUDY_PHARM: List[_CSU_C09_STUDY_PHARM] = Field(
        default=...,
        title="STUDY_PHARM",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
