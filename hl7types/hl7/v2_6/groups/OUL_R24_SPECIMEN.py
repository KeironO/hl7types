"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: OUL_R24.SPECIMEN
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.OBX import OBX
from ..segments.SPM import SPM

from .OUL_R24_CONTAINER import OUL_R24_CONTAINER

_OBX = OBX
_OUL_R24_CONTAINER = OUL_R24_CONTAINER
_SPM = SPM


class OUL_R24_SPECIMEN(BaseModel):
    """HL7 v2 OUL_R24.SPECIMEN group.

    Attributes:
        SPM (SPM): required
        OBX (Optional[List[OBX]]): optional
        CONTAINER (Optional[List[OUL_R24_CONTAINER]]): optional
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

    CONTAINER: Optional[List[_OUL_R24_CONTAINER]] = Field(
        default=None,
        title="CONTAINER",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
