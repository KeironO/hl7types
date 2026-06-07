"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: OPR_O38.SPECIMEN
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.OBX import OBX
from ..segments.SAC import SAC
from ..segments.SPM import SPM

from .OPR_O38_OBSERVATION_REQUEST import OPR_O38_OBSERVATION_REQUEST
from .OPR_O38_TIMING import OPR_O38_TIMING

_OBX = OBX
_OPR_O38_OBSERVATION_REQUEST = OPR_O38_OBSERVATION_REQUEST
_OPR_O38_TIMING = OPR_O38_TIMING
_SAC = SAC
_SPM = SPM


class OPR_O38_SPECIMEN(HL7Model):
    """HL7 v2 OPR_O38.SPECIMEN group.

    Attributes:
        SPM (SPM): required
        OBX (Optional[List[OBX]]): optional
        SAC (Optional[List[SAC]]): optional
        OBSERVATION_REQUEST (Optional[List[OPR_O38_OBSERVATION_REQUEST]]): optional
        TIMING (Optional[List[OPR_O38_TIMING]]): optional
    """

    SPM: _SPM = Field(
        title="SPM",
        description="Required",
    )

    OBX: Optional[List[_OBX]] = Field(
        default=None,
        title="OBX",
        description="Optional, repeating",
    )

    SAC: Optional[List[_SAC]] = Field(
        default=None,
        title="SAC",
        description="Optional, repeating",
    )

    OBSERVATION_REQUEST: Optional[List[_OPR_O38_OBSERVATION_REQUEST]] = Field(
        default=None,
        title="OBSERVATION_REQUEST",
        description="Optional, repeating",
    )

    TIMING: Optional[List[_OPR_O38_TIMING]] = Field(
        default=None,
        title="TIMING",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
