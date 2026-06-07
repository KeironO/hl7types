"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: OSM_R26.CONTAINER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.SAC import SAC

from .OSM_R26_CONTAINER_OBSERVATION import OSM_R26_CONTAINER_OBSERVATION

_OSM_R26_CONTAINER_OBSERVATION = OSM_R26_CONTAINER_OBSERVATION
_SAC = SAC


class OSM_R26_CONTAINER(HL7Model):
    """HL7 v2 OSM_R26.CONTAINER group.

    Attributes:
        SAC (SAC): required
        CONTAINER_OBSERVATION (Optional[List[OSM_R26_CONTAINER_OBSERVATION]]): optional
    """

    SAC: _SAC = Field(
        title="SAC",
        description="Required",
    )

    CONTAINER_OBSERVATION: Optional[List[_OSM_R26_CONTAINER_OBSERVATION]] = Field(
        default=None,
        title="CONTAINER_OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
