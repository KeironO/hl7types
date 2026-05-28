"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: SSU_U03.SPECIMEN
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.OBX import OBX
from ..segments.SPM import SPM

_OBX = OBX
_SPM = SPM


class SSU_U03_SPECIMEN(BaseModel):
    """HL7 v2 SSU_U03.SPECIMEN group.

    Attributes:
        SPM (SPM): required
        OBX (Optional[List[OBX]]): optional
    """

    SPM: _SPM = Field(
        default=...,
        title="SPM",
        description="Required",
    )

    OBX: Optional[List[_OBX]] = Field(
        default=None,
        title="OBX",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
