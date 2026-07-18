"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: OUL_R23.SPECIMEN
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.SPM import SPM

from .OUL_R23_CONTAINER import OUL_R23_CONTAINER
from .OUL_R23_SPECIMEN_OBSERVATION import OUL_R23_SPECIMEN_OBSERVATION

_OUL_R23_CONTAINER = OUL_R23_CONTAINER
_OUL_R23_SPECIMEN_OBSERVATION = OUL_R23_SPECIMEN_OBSERVATION
_SPM = SPM


class OUL_R23_SPECIMEN(HL7Model):
    """HL7 v2 OUL_R23.SPECIMEN group.

    Attributes:
        SPM (SPM): Specimen, required
        SPECIMEN_OBSERVATION (Optional[List[OUL_R23_SPECIMEN_OBSERVATION]]): optional
        CONTAINER (List[OUL_R23_CONTAINER]): required
    """

    SPM: _SPM = Field(
        title="SPM",
        description="Specimen",
    )

    SPECIMEN_OBSERVATION: Optional[List[_OUL_R23_SPECIMEN_OBSERVATION]] = Field(
        default=None,
        title="SPECIMEN_OBSERVATION",
    )

    CONTAINER: List[_OUL_R23_CONTAINER] = Field(
        min_length=1,
        title="CONTAINER",
    )

    model_config = ConfigDict(populate_by_name=True)
