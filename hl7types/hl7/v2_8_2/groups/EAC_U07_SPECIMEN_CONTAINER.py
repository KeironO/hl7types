"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: EAC_U07.SPECIMEN_CONTAINER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.OBR import OBR
from ..segments.SAC import SAC
from ..segments.SPM import SPM

_OBR = OBR
_SAC = SAC
_SPM = SPM


class EAC_U07_SPECIMEN_CONTAINER(BaseModel):
    """HL7 v2 EAC_U07.SPECIMEN_CONTAINER group.

    Attributes:
        SAC (SAC): required
        OBR (Optional[List[OBR]]): optional
        SPM (Optional[List[SPM]]): optional
    """

    SAC: _SAC = Field(
        default=...,
        title="SAC",
        description="Required",
    )

    OBR: Optional[List[_OBR]] = Field(
        default=None,
        title="OBR",
        description="Optional, repeating",
    )

    SPM: Optional[List[_SPM]] = Field(
        default=None,
        title="SPM",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
