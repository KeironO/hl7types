"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: EAC_U07.SPECIMEN_CONTAINER
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.SAC import SAC
from ..segments.SPM import SPM

_SAC = SAC
_SPM = SPM


class EAC_U07_SPECIMEN_CONTAINER(BaseModel):
    """HL7 v2 EAC_U07.SPECIMEN_CONTAINER group.

    Attributes:
        SAC (SAC): required
        SPM (Optional[List[SPM]]): optional
    """

    SAC: _SAC = Field(
        default=...,
        title="SAC",
        description="Required",
    )

    SPM: list[_SPM] | None = Field(
        default=None,
        title="SPM",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
