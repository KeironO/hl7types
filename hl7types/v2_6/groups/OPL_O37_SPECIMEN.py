"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: OPL_O37.SPECIMEN
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.OBX import OBX
from ..segments.SPM import SPM

from .OPL_O37_CONTAINER import OPL_O37_CONTAINER
from .OPL_O37_OBSERVATION_REQUEST import OPL_O37_OBSERVATION_REQUEST

_OBX = OBX
_OPL_O37_CONTAINER = OPL_O37_CONTAINER
_OPL_O37_OBSERVATION_REQUEST = OPL_O37_OBSERVATION_REQUEST
_SPM = SPM


class OPL_O37_SPECIMEN(BaseModel):
    """HL7 v2 OPL_O37.SPECIMEN group.

    Attributes:
        SPM (SPM): required
        OBX (Optional[List[OBX]]): optional
        CONTAINER (Optional[List[OPL_O37_CONTAINER]]): optional
        OBSERVATION_REQUEST (List[OPL_O37_OBSERVATION_REQUEST]): required
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

    CONTAINER: Optional[List[_OPL_O37_CONTAINER]] = Field(
        default=None,
        title="CONTAINER",
        description="Optional, repeating",
    )

    OBSERVATION_REQUEST: List[_OPL_O37_OBSERVATION_REQUEST] = Field(
        default=...,
        title="OBSERVATION_REQUEST",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
