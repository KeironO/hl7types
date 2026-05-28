"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: OML_O39.SPECIMEN_IN_PACKAGE
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.SPM import SPM

from .OML_O39_SPECIMEN_CONTAINER_IN_PACKAGE import OML_O39_SPECIMEN_CONTAINER_IN_PACKAGE
from .OML_O39_SPECIMEN_OBSERVATION import OML_O39_SPECIMEN_OBSERVATION

_OML_O39_SPECIMEN_CONTAINER_IN_PACKAGE = OML_O39_SPECIMEN_CONTAINER_IN_PACKAGE
_OML_O39_SPECIMEN_OBSERVATION = OML_O39_SPECIMEN_OBSERVATION
_SPM = SPM


class OML_O39_SPECIMEN_IN_PACKAGE(BaseModel):
    """HL7 v2 OML_O39.SPECIMEN_IN_PACKAGE group.

    Attributes:
        SPM (SPM): required
        SPECIMEN_OBSERVATION (Optional[List[OML_O39_SPECIMEN_OBSERVATION]]): optional
        SPECIMEN_CONTAINER_IN_PACKAGE (Optional[List[OML_O39_SPECIMEN_CONTAINER_IN_PACKAGE]]): optional
    """

    SPM: _SPM = Field(
        default=...,
        title="SPM",
        description="Required",
    )

    SPECIMEN_OBSERVATION: Optional[List[_OML_O39_SPECIMEN_OBSERVATION]] = Field(
        default=None,
        title="SPECIMEN_OBSERVATION",
        description="Optional, repeating",
    )

    SPECIMEN_CONTAINER_IN_PACKAGE: Optional[List[_OML_O39_SPECIMEN_CONTAINER_IN_PACKAGE]] = Field(
        default=None,
        title="SPECIMEN_CONTAINER_IN_PACKAGE",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
