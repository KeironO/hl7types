"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: OPR_O38.SPECIMEN
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.SAC import SAC
from ..segments.SPM import SPM

from .OPR_O38_OBSERVATION_REQUEST import OPR_O38_OBSERVATION_REQUEST
from .OPR_O38_SPECIMEN_OBSERVATION import OPR_O38_SPECIMEN_OBSERVATION
from .OPR_O38_TIMING import OPR_O38_TIMING

_OPR_O38_OBSERVATION_REQUEST = OPR_O38_OBSERVATION_REQUEST
_OPR_O38_SPECIMEN_OBSERVATION = OPR_O38_SPECIMEN_OBSERVATION
_OPR_O38_TIMING = OPR_O38_TIMING
_SAC = SAC
_SPM = SPM


class OPR_O38_SPECIMEN(HL7Model):
    """HL7 v2 OPR_O38.SPECIMEN group.

    Attributes:
        SPM (SPM): Specimen, required
        SPECIMEN_OBSERVATION (Optional[List[OPR_O38_SPECIMEN_OBSERVATION]]): optional
        SAC (Optional[List[SAC]]): Specimen Container detail, optional
        OBSERVATION_REQUEST (Optional[List[OPR_O38_OBSERVATION_REQUEST]]): optional
        TIMING (Optional[List[OPR_O38_TIMING]]): optional
    """

    SPM: _SPM = Field(
        title="SPM",
        description="Specimen",
    )

    SPECIMEN_OBSERVATION: Optional[List[_OPR_O38_SPECIMEN_OBSERVATION]] = Field(
        default=None,
        title="SPECIMEN_OBSERVATION",
    )

    SAC: Optional[List[_SAC]] = Field(
        default=None,
        title="SAC",
        description="Specimen Container detail",
    )

    OBSERVATION_REQUEST: Optional[List[_OPR_O38_OBSERVATION_REQUEST]] = Field(
        default=None,
        title="OBSERVATION_REQUEST",
    )

    TIMING: Optional[List[_OPR_O38_TIMING]] = Field(
        default=None,
        title="TIMING",
    )

    model_config = ConfigDict(populate_by_name=True)
