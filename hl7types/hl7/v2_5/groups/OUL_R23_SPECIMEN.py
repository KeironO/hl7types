"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: OUL_R23.SPECIMEN
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.OBX import OBX
from ..segments.SPM import SPM
from .OUL_R23_CONTAINER import OUL_R23_CONTAINER

_OBX = OBX
_OUL_R23_CONTAINER = OUL_R23_CONTAINER
_SPM = SPM


class OUL_R23_SPECIMEN(BaseModel):
    """HL7 v2 OUL_R23.SPECIMEN group.

    Attributes:
        SPM (SPM): required
        OBX (Optional[List[OBX]]): optional
        CONTAINER (List[OUL_R23_CONTAINER]): required
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

    CONTAINER: list[_OUL_R23_CONTAINER] = Field(
        default=...,
        title="CONTAINER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
