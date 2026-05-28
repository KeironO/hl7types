"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: OPL_O37.SPECIMEN
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.SPM import SPM
from .OPL_O37_CONTAINER import OPL_O37_CONTAINER
from .OPL_O37_OBSERVATION_REQUEST import OPL_O37_OBSERVATION_REQUEST
from .OPL_O37_SPECIMEN_OBSERVATION import OPL_O37_SPECIMEN_OBSERVATION

_OPL_O37_CONTAINER = OPL_O37_CONTAINER
_OPL_O37_OBSERVATION_REQUEST = OPL_O37_OBSERVATION_REQUEST
_OPL_O37_SPECIMEN_OBSERVATION = OPL_O37_SPECIMEN_OBSERVATION
_SPM = SPM


class OPL_O37_SPECIMEN(BaseModel):
    """HL7 v2 OPL_O37.SPECIMEN group.

    Attributes:
        SPM (SPM): required
        SPECIMEN_OBSERVATION (Optional[List[OPL_O37_SPECIMEN_OBSERVATION]]): optional
        CONTAINER (Optional[List[OPL_O37_CONTAINER]]): optional
        OBSERVATION_REQUEST (List[OPL_O37_OBSERVATION_REQUEST]): required
    """

    SPM: _SPM = Field(
        default=...,
        title="SPM",
        description="Required",
    )

    SPECIMEN_OBSERVATION: list[_OPL_O37_SPECIMEN_OBSERVATION] | None = Field(
        default=None,
        title="SPECIMEN_OBSERVATION",
        description="Optional, repeating",
    )

    CONTAINER: list[_OPL_O37_CONTAINER] | None = Field(
        default=None,
        title="CONTAINER",
        description="Optional, repeating",
    )

    OBSERVATION_REQUEST: list[_OPL_O37_OBSERVATION_REQUEST] = Field(
        default=...,
        title="OBSERVATION_REQUEST",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
