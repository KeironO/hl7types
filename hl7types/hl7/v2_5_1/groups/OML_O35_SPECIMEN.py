"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: OML_O35.SPECIMEN
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.OBX import OBX
from ..segments.SPM import SPM
from .OML_O35_SPECIMEN_CONTAINER import OML_O35_SPECIMEN_CONTAINER

_OBX = OBX
_OML_O35_SPECIMEN_CONTAINER = OML_O35_SPECIMEN_CONTAINER
_SPM = SPM


class OML_O35_SPECIMEN(BaseModel):
    """HL7 v2 OML_O35.SPECIMEN group.

    Attributes:
        SPM (SPM): required
        OBX (Optional[List[OBX]]): optional
        SPECIMEN_CONTAINER (List[OML_O35_SPECIMEN_CONTAINER]): required
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

    SPECIMEN_CONTAINER: list[_OML_O35_SPECIMEN_CONTAINER] = Field(
        default=...,
        title="SPECIMEN_CONTAINER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
