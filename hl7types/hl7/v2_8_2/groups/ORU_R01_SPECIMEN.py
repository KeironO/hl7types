"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: ORU_R01.SPECIMEN
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.SPM import SPM

from .ORU_R01_SPECIMEN_OBSERVATION import ORU_R01_SPECIMEN_OBSERVATION

_ORU_R01_SPECIMEN_OBSERVATION = ORU_R01_SPECIMEN_OBSERVATION
_SPM = SPM


class ORU_R01_SPECIMEN(BaseModel):
    """HL7 v2 ORU_R01.SPECIMEN group.

    Attributes:
        SPM (SPM): required
        SPECIMEN_OBSERVATION (Optional[List[ORU_R01_SPECIMEN_OBSERVATION]]): optional
    """

    SPM: _SPM = Field(
        default=...,
        title="SPM",
        description="Required",
    )

    SPECIMEN_OBSERVATION: Optional[List[_ORU_R01_SPECIMEN_OBSERVATION]] = Field(
        default=None,
        title="SPECIMEN_OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
