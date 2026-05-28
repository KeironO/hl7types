"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: OML_O21.CONTAINER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.SAC import SAC

from .OML_O21_CONTAINER_OBSERVATION import OML_O21_CONTAINER_OBSERVATION

_OML_O21_CONTAINER_OBSERVATION = OML_O21_CONTAINER_OBSERVATION
_SAC = SAC


class OML_O21_CONTAINER(BaseModel):
    """HL7 v2 OML_O21.CONTAINER group.

    Attributes:
        SAC (SAC): required
        CONTAINER_OBSERVATION (Optional[List[OML_O21_CONTAINER_OBSERVATION]]): optional
    """

    SAC: _SAC = Field(
        default=...,
        title="SAC",
        description="Required",
    )

    CONTAINER_OBSERVATION: Optional[List[_OML_O21_CONTAINER_OBSERVATION]] = Field(
        default=None,
        title="CONTAINER_OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
