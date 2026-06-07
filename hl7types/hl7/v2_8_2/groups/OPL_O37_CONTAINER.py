"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: OPL_O37.CONTAINER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.SAC import SAC

from .OPL_O37_CONTAINER_OBSERVATION import OPL_O37_CONTAINER_OBSERVATION

_OPL_O37_CONTAINER_OBSERVATION = OPL_O37_CONTAINER_OBSERVATION
_SAC = SAC


class OPL_O37_CONTAINER(HL7Model):
    """HL7 v2 OPL_O37.CONTAINER group.

    Attributes:
        SAC (SAC): required
        CONTAINER_OBSERVATION (Optional[List[OPL_O37_CONTAINER_OBSERVATION]]): optional
    """

    SAC: _SAC = Field(
        title="SAC",
        description="Required",
    )

    CONTAINER_OBSERVATION: Optional[List[_OPL_O37_CONTAINER_OBSERVATION]] = Field(
        default=None,
        title="CONTAINER_OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
