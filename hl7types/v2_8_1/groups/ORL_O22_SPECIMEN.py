"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: ORL_O22.SPECIMEN
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.SAC import SAC
from ..segments.SPM import SPM

_SAC = SAC
_SPM = SPM


class ORL_O22_SPECIMEN(BaseModel):
    """HL7 v2 ORL_O22.SPECIMEN group.

    Attributes:
        SPM (SPM): required
        SAC (Optional[List[SAC]]): optional
    """

    SPM: _SPM = Field(
        default=...,
        title="SPM",
        description="Required",
    )

    SAC: Optional[List[_SAC]] = Field(
        default=None,
        title="SAC",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
