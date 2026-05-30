"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: OMG_O19.SPECIMEN
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.SPM import SPM

from .OMG_O19_CONTAINER import OMG_O19_CONTAINER
from .OMG_O19_SPECIMEN_OBSERVATION import OMG_O19_SPECIMEN_OBSERVATION

_OMG_O19_CONTAINER = OMG_O19_CONTAINER
_OMG_O19_SPECIMEN_OBSERVATION = OMG_O19_SPECIMEN_OBSERVATION
_SPM = SPM


class OMG_O19_SPECIMEN(HL7Model):
    """HL7 v2 OMG_O19.SPECIMEN group.

    Attributes:
        SPM (SPM): required
        SPECIMEN_OBSERVATION (Optional[List[OMG_O19_SPECIMEN_OBSERVATION]]): optional
        CONTAINER (Optional[List[OMG_O19_CONTAINER]]): optional
    """

    SPM: _SPM = Field(
        default=...,
        title="SPM",
        description="Required",
    )

    SPECIMEN_OBSERVATION: Optional[List[_OMG_O19_SPECIMEN_OBSERVATION]] = Field(
        default=None,
        title="SPECIMEN_OBSERVATION",
        description="Optional, repeating",
    )

    CONTAINER: Optional[List[_OMG_O19_CONTAINER]] = Field(
        default=None,
        title="CONTAINER",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
