"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: ORL_O42.SPECIMEN
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.SAC import SAC
from ..segments.SPM import SPM

from .ORL_O42_ORDER import ORL_O42_ORDER
from .ORL_O42_SPECIMEN_OBSERVATION import ORL_O42_SPECIMEN_OBSERVATION

_ORL_O42_ORDER = ORL_O42_ORDER
_ORL_O42_SPECIMEN_OBSERVATION = ORL_O42_SPECIMEN_OBSERVATION
_SAC = SAC
_SPM = SPM


class ORL_O42_SPECIMEN(BaseModel):
    """HL7 v2 ORL_O42.SPECIMEN group.

    Attributes:
        SPM (SPM): required
        SPECIMEN_OBSERVATION (Optional[List[ORL_O42_SPECIMEN_OBSERVATION]]): optional
        SAC (Optional[List[SAC]]): optional
        ORDER (Optional[List[ORL_O42_ORDER]]): optional
    """

    SPM: _SPM = Field(
        default=...,
        title="SPM",
        description="Required",
    )

    SPECIMEN_OBSERVATION: Optional[List[_ORL_O42_SPECIMEN_OBSERVATION]] = Field(
        default=None,
        title="SPECIMEN_OBSERVATION",
        description="Optional, repeating",
    )

    SAC: Optional[List[_SAC]] = Field(
        default=None,
        title="SAC",
        description="Optional, repeating",
    )

    ORDER: Optional[List[_ORL_O42_ORDER]] = Field(
        default=None,
        title="ORDER",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
