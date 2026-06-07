"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: OML_O39.SPECIMEN_CONTAINER_IN_PACKAGE
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.SAC import SAC

from .OML_O39_CONTAINER_OBSERVATION import OML_O39_CONTAINER_OBSERVATION

_OML_O39_CONTAINER_OBSERVATION = OML_O39_CONTAINER_OBSERVATION
_SAC = SAC


class OML_O39_SPECIMEN_CONTAINER_IN_PACKAGE(HL7Model):
    """HL7 v2 OML_O39.SPECIMEN_CONTAINER_IN_PACKAGE group.

    Attributes:
        SAC (SAC): required
        CONTAINER_OBSERVATION (Optional[List[OML_O39_CONTAINER_OBSERVATION]]): optional
    """

    SAC: _SAC = Field(
        title="SAC",
        description="Required",
    )

    CONTAINER_OBSERVATION: Optional[List[_OML_O39_CONTAINER_OBSERVATION]] = Field(
        default=None,
        title="CONTAINER_OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
