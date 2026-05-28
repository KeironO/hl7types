"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: ORG_O20.SPECIMEN
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.SAC import SAC
from ..segments.SPM import SPM

_SAC = SAC
_SPM = SPM


class ORG_O20_SPECIMEN(BaseModel):
    """HL7 v2 ORG_O20.SPECIMEN group.

    Attributes:
        SPM (SPM): required
        SAC (Optional[List[SAC]]): optional
    """

    SPM: _SPM = Field(
        default=...,
        title="SPM",
        description="Required",
    )

    SAC: list[_SAC] | None = Field(
        default=None,
        title="SAC",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
