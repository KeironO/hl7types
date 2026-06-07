"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: OMG_O19.CONTAINER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.SAC import SAC

from .OMG_O19_CONTAINER_OBSERVATION import OMG_O19_CONTAINER_OBSERVATION

_OMG_O19_CONTAINER_OBSERVATION = OMG_O19_CONTAINER_OBSERVATION
_SAC = SAC


class OMG_O19_CONTAINER(HL7Model):
    """HL7 v2 OMG_O19.CONTAINER group.

    Attributes:
        SAC (SAC): required
        CONTAINER_OBSERVATION (Optional[List[OMG_O19_CONTAINER_OBSERVATION]]): optional
    """

    SAC: _SAC = Field(
        title="SAC",
        description="Required",
    )

    CONTAINER_OBSERVATION: Optional[List[_OMG_O19_CONTAINER_OBSERVATION]] = Field(
        default=None,
        title="CONTAINER_OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
