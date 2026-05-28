"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: OMG_O19.SPECIMEN
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.OBX import OBX
from ..segments.SPM import SPM
from .OMG_O19_CONTAINER import OMG_O19_CONTAINER

_OBX = OBX
_OMG_O19_CONTAINER = OMG_O19_CONTAINER
_SPM = SPM


class OMG_O19_SPECIMEN(BaseModel):
    """HL7 v2 OMG_O19.SPECIMEN group.

    Attributes:
        SPM (SPM): required
        OBX (Optional[List[OBX]]): optional
        CONTAINER (Optional[List[OMG_O19_CONTAINER]]): optional
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

    CONTAINER: list[_OMG_O19_CONTAINER] | None = Field(
        default=None,
        title="CONTAINER",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
