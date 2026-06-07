"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: CSU_C09.STUDY_SCHEDULE
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.CSS import CSS

from .CSU_C09_ORCRXARXR_SUPPGRP import CSU_C09_ORCRXARXR_SUPPGRP
from .CSU_C09_STUDY_OBSERVATION import CSU_C09_STUDY_OBSERVATION

_CSS = CSS
_CSU_C09_ORCRXARXR_SUPPGRP = CSU_C09_ORCRXARXR_SUPPGRP
_CSU_C09_STUDY_OBSERVATION = CSU_C09_STUDY_OBSERVATION


class CSU_C09_STUDY_SCHEDULE(HL7Model):
    """HL7 v2 CSU_C09.STUDY_SCHEDULE group.

    Attributes:
        CSS (Optional[CSS]): optional
        STUDY_OBSERVATION (List[CSU_C09_STUDY_OBSERVATION]): required
        ORCRXARXR_SUPPGRP (List[CSU_C09_ORCRXARXR_SUPPGRP]): required
    """

    CSS: Optional[_CSS] = Field(
        default=None,
        title="CSS",
        description="Optional",
    )

    STUDY_OBSERVATION: List[_CSU_C09_STUDY_OBSERVATION] = Field(
        min_length=1,
        title="STUDY_OBSERVATION",
        description="Required, repeating",
    )

    ORCRXARXR_SUPPGRP: List[_CSU_C09_ORCRXARXR_SUPPGRP] = Field(
        min_length=1,
        title="ORCRXARXR_SUPPGRP",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
