"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: CSU_C09.STUDY_SCHEDULE
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.CSS import CSS

from .CSU_C09_STUDY_OBSERVATION import CSU_C09_STUDY_OBSERVATION
from .CSU_C09_STUDY_PHARM import CSU_C09_STUDY_PHARM

_CSS = CSS
_CSU_C09_STUDY_OBSERVATION = CSU_C09_STUDY_OBSERVATION
_CSU_C09_STUDY_PHARM = CSU_C09_STUDY_PHARM


class CSU_C09_STUDY_SCHEDULE(HL7Model):
    """HL7 v2 CSU_C09.STUDY_SCHEDULE group.

    Attributes:
        CSS (Optional[CSS]): optional
        STUDY_OBSERVATION (Optional[List[CSU_C09_STUDY_OBSERVATION]]): optional
        STUDY_PHARM (List[CSU_C09_STUDY_PHARM]): required
    """

    CSS: Optional[_CSS] = Field(
        default=None,
        title="CSS",
        description="Optional",
    )

    STUDY_OBSERVATION: Optional[List[_CSU_C09_STUDY_OBSERVATION]] = Field(
        default=None,
        title="STUDY_OBSERVATION",
        description="Optional, repeating",
    )

    STUDY_PHARM: List[_CSU_C09_STUDY_PHARM] = Field(
        default=...,
        title="STUDY_PHARM",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
