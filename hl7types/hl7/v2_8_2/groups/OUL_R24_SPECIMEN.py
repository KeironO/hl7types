"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: OUL_R24.SPECIMEN
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.SPM import SPM

from .OUL_R24_CONTAINER import OUL_R24_CONTAINER
from .OUL_R24_SPECIMEN_OBSERVATION import OUL_R24_SPECIMEN_OBSERVATION

_OUL_R24_CONTAINER = OUL_R24_CONTAINER
_OUL_R24_SPECIMEN_OBSERVATION = OUL_R24_SPECIMEN_OBSERVATION
_SPM = SPM


class OUL_R24_SPECIMEN(HL7Model):
    """HL7 v2 OUL_R24.SPECIMEN group.

    Attributes:
        SPM (SPM): Specimen, required
        SPECIMEN_OBSERVATION (Optional[List[OUL_R24_SPECIMEN_OBSERVATION]]): optional
        CONTAINER (Optional[List[OUL_R24_CONTAINER]]): optional
    """

    SPM: _SPM = Field(
        title="SPM",
        description="Specimen",
    )

    SPECIMEN_OBSERVATION: Optional[List[_OUL_R24_SPECIMEN_OBSERVATION]] = Field(
        default=None,
        title="SPECIMEN_OBSERVATION",
    )

    CONTAINER: Optional[List[_OUL_R24_CONTAINER]] = Field(
        default=None,
        title="CONTAINER",
    )

    model_config = {"populate_by_name": True}
