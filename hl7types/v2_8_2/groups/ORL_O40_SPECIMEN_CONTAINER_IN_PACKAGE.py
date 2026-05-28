"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: ORL_O40.SPECIMEN_CONTAINER_IN_PACKAGE
Type: Group
"""
from _future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field

from ..segments.SAC import SAC

_SAC = SAC


class ORL_O40_SPECIMEN_CONTAINER_IN_PACKAGE(BaseModel):
    """HL7 v2 ORL_O40.SPECIMEN_CONTAINER_IN_PACKAGE group.

    Attributes:
        SAC (SAC): required
    """

    SAC: _SAC = Field(
        default=...,
        title="SAC",
        description="Required",
    )

    model_config = {"populate_by_name": True}
