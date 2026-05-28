"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: RSP_Z90.SPECIMEN
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.OBX import OBX
from ..segments.SPM import SPM

_OBX = OBX
_SPM = SPM


class RSP_Z90_SPECIMEN(BaseModel):
    """HL7 v2 RSP_Z90.SPECIMEN group.

    Attributes:
        SPM (SPM): required
        OBX (Optional[List[OBX]]): optional
    """

    SPM: _SPM = Field(
        default=...,
        title="SPM",
        description="Required",
    )

    OBX: list[_OBX] | None = Field(
        default=None,
        title="OBX",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
