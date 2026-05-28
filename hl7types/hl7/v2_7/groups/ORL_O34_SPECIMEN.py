"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: ORL_O34.SPECIMEN
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.SAC import SAC
from ..segments.SPM import SPM
from .ORL_O34_ORDER import ORL_O34_ORDER
from .ORL_O34_SPECIMEN_OBSERVATION import ORL_O34_SPECIMEN_OBSERVATION

_ORL_O34_ORDER = ORL_O34_ORDER
_ORL_O34_SPECIMEN_OBSERVATION = ORL_O34_SPECIMEN_OBSERVATION
_SAC = SAC
_SPM = SPM


class ORL_O34_SPECIMEN(BaseModel):
    """HL7 v2 ORL_O34.SPECIMEN group.

    Attributes:
        SPM (SPM): required
        SPECIMEN_OBSERVATION (Optional[List[ORL_O34_SPECIMEN_OBSERVATION]]): optional
        SAC (Optional[List[SAC]]): optional
        ORDER (Optional[List[ORL_O34_ORDER]]): optional
    """

    SPM: _SPM = Field(
        default=...,
        title="SPM",
        description="Required",
    )

    SPECIMEN_OBSERVATION: list[_ORL_O34_SPECIMEN_OBSERVATION] | None = Field(
        default=None,
        title="SPECIMEN_OBSERVATION",
        description="Optional, repeating",
    )

    SAC: list[_SAC] | None = Field(
        default=None,
        title="SAC",
        description="Optional, repeating",
    )

    ORDER: list[_ORL_O34_ORDER] | None = Field(
        default=None,
        title="ORDER",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
