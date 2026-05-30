"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: OML_O21.SPECIMEN
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.SPM import SPM

from .OML_O21_CONTAINER import OML_O21_CONTAINER
from .OML_O21_SPECIMEN_OBSERVATION import OML_O21_SPECIMEN_OBSERVATION

_OML_O21_CONTAINER = OML_O21_CONTAINER
_OML_O21_SPECIMEN_OBSERVATION = OML_O21_SPECIMEN_OBSERVATION
_SPM = SPM


class OML_O21_SPECIMEN(HL7Model):
    """HL7 v2 OML_O21.SPECIMEN group.

    Attributes:
        SPM (SPM): required
        SPECIMEN_OBSERVATION (Optional[List[OML_O21_SPECIMEN_OBSERVATION]]): optional
        CONTAINER (Optional[List[OML_O21_CONTAINER]]): optional
    """

    SPM: _SPM = Field(
        default=...,
        title="SPM",
        description="Required",
    )

    SPECIMEN_OBSERVATION: Optional[List[_OML_O21_SPECIMEN_OBSERVATION]] = Field(
        default=None,
        title="SPECIMEN_OBSERVATION",
        description="Optional, repeating",
    )

    CONTAINER: Optional[List[_OML_O21_CONTAINER]] = Field(
        default=None,
        title="CONTAINER",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
