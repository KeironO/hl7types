"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: OPU_R25.SPECIMEN
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.SPM import SPM

from .OPU_R25_CONTAINER import OPU_R25_CONTAINER
from .OPU_R25_ORDER import OPU_R25_ORDER
from .OPU_R25_SPECIMEN_OBSERVATION import OPU_R25_SPECIMEN_OBSERVATION

_OPU_R25_CONTAINER = OPU_R25_CONTAINER
_OPU_R25_ORDER = OPU_R25_ORDER
_OPU_R25_SPECIMEN_OBSERVATION = OPU_R25_SPECIMEN_OBSERVATION
_SPM = SPM


class OPU_R25_SPECIMEN(HL7Model):
    """HL7 v2 OPU_R25.SPECIMEN group.

    Attributes:
        SPM (SPM): required
        SPECIMEN_OBSERVATION (Optional[List[OPU_R25_SPECIMEN_OBSERVATION]]): optional
        CONTAINER (Optional[List[OPU_R25_CONTAINER]]): optional
        ORDER (List[OPU_R25_ORDER]): required
    """

    SPM: _SPM = Field(
        default=...,
        title="SPM",
        description="Required",
    )

    SPECIMEN_OBSERVATION: Optional[List[_OPU_R25_SPECIMEN_OBSERVATION]] = Field(
        default=None,
        title="SPECIMEN_OBSERVATION",
        description="Optional, repeating",
    )

    CONTAINER: Optional[List[_OPU_R25_CONTAINER]] = Field(
        default=None,
        title="CONTAINER",
        description="Optional, repeating",
    )

    ORDER: List[_OPU_R25_ORDER] = Field(
        default=...,
        title="ORDER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
