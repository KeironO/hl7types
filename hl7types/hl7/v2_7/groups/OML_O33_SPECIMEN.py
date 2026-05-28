"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: OML_O33.SPECIMEN
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.SAC import SAC
from ..segments.SPM import SPM
from .OML_O33_ORDER import OML_O33_ORDER
from .OML_O33_SPECIMEN_OBSERVATION import OML_O33_SPECIMEN_OBSERVATION

_OML_O33_ORDER = OML_O33_ORDER
_OML_O33_SPECIMEN_OBSERVATION = OML_O33_SPECIMEN_OBSERVATION
_SAC = SAC
_SPM = SPM


class OML_O33_SPECIMEN(BaseModel):
    """HL7 v2 OML_O33.SPECIMEN group.

    Attributes:
        SPM (SPM): required
        SPECIMEN_OBSERVATION (Optional[List[OML_O33_SPECIMEN_OBSERVATION]]): optional
        SAC (Optional[List[SAC]]): optional
        ORDER (List[OML_O33_ORDER]): required
    """

    SPM: _SPM = Field(
        default=...,
        title="SPM",
        description="Required",
    )

    SPECIMEN_OBSERVATION: list[_OML_O33_SPECIMEN_OBSERVATION] | None = Field(
        default=None,
        title="SPECIMEN_OBSERVATION",
        description="Optional, repeating",
    )

    SAC: list[_SAC] | None = Field(
        default=None,
        title="SAC",
        description="Optional, repeating",
    )

    ORDER: list[_OML_O33_ORDER] = Field(
        default=...,
        title="ORDER",
        description="Required, repeating",
    )

    model_config = {"populate_by_name": True}
