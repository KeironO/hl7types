"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: PPG_PCG.PATHWAY
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.PTH import PTH
from ..segments.VAR import VAR
from .PPG_PCG_GOAL import PPG_PCG_GOAL
from .PPG_PCG_PATHWAY_ROLE import PPG_PCG_PATHWAY_ROLE

_NTE = NTE
_PPG_PCG_GOAL = PPG_PCG_GOAL
_PPG_PCG_PATHWAY_ROLE = PPG_PCG_PATHWAY_ROLE
_PTH = PTH
_VAR = VAR


class PPG_PCG_PATHWAY(BaseModel):
    """HL7 v2 PPG_PCG.PATHWAY group.

    Attributes:
        PTH (PTH): required
        NTE (Optional[List[NTE]]): optional
        VAR (Optional[List[VAR]]): optional
        PATHWAY_ROLE (Optional[List[PPG_PCG_PATHWAY_ROLE]]): optional
        GOAL (Optional[List[PPG_PCG_GOAL]]): optional
    """

    PTH: _PTH = Field(
        default=...,
        title="PTH",
        description="Required",
    )

    NTE: list[_NTE] | None = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    VAR: list[_VAR] | None = Field(
        default=None,
        title="VAR",
        description="Optional, repeating",
    )

    PATHWAY_ROLE: list[_PPG_PCG_PATHWAY_ROLE] | None = Field(
        default=None,
        title="PATHWAY_ROLE",
        description="Optional, repeating",
    )

    GOAL: list[_PPG_PCG_GOAL] | None = Field(
        default=None,
        title="GOAL",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
