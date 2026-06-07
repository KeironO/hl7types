"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: OML_O35.SPECIMEN
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.SPM import SPM

from .OML_O35_SPECIMEN_CONTAINER import OML_O35_SPECIMEN_CONTAINER
from .OML_O35_SPECIMEN_OBSERVATION import OML_O35_SPECIMEN_OBSERVATION

_OML_O35_SPECIMEN_CONTAINER = OML_O35_SPECIMEN_CONTAINER
_OML_O35_SPECIMEN_OBSERVATION = OML_O35_SPECIMEN_OBSERVATION
_SPM = SPM


class OML_O35_SPECIMEN(HL7Model):
    """HL7 v2 OML_O35.SPECIMEN group.

    Attributes:
        SPM (SPM): required
        SPECIMEN_OBSERVATION (Optional[List[OML_O35_SPECIMEN_OBSERVATION]]): optional
        SPECIMEN_CONTAINER (List[OML_O35_SPECIMEN_CONTAINER]): required
    """

    SPM: _SPM = Field(
        title="SPM",
        description="Required",
    )

    SPECIMEN_OBSERVATION: Optional[List[_OML_O35_SPECIMEN_OBSERVATION]] = Field(
        default=None,
        title="SPECIMEN_OBSERVATION",
        description="Optional, repeating",
    )

    SPECIMEN_CONTAINER: List[_OML_O35_SPECIMEN_CONTAINER] = Field(
        min_length=1,
        title="SPECIMEN_CONTAINER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
