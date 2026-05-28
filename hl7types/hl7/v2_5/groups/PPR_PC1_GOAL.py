"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: PPR_PC1.GOAL
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.GOL import GOL
from ..segments.NTE import NTE
from ..segments.VAR import VAR
from .PPR_PC1_GOAL_OBSERVATION import PPR_PC1_GOAL_OBSERVATION
from .PPR_PC1_GOAL_ROLE import PPR_PC1_GOAL_ROLE

_GOL = GOL
_NTE = NTE
_PPR_PC1_GOAL_OBSERVATION = PPR_PC1_GOAL_OBSERVATION
_PPR_PC1_GOAL_ROLE = PPR_PC1_GOAL_ROLE
_VAR = VAR


class PPR_PC1_GOAL(BaseModel):
    """HL7 v2 PPR_PC1.GOAL group.

    Attributes:
        GOL (GOL): required
        NTE (Optional[List[NTE]]): optional
        VAR (Optional[List[VAR]]): optional
        GOAL_ROLE (Optional[List[PPR_PC1_GOAL_ROLE]]): optional
        GOAL_OBSERVATION (Optional[List[PPR_PC1_GOAL_OBSERVATION]]): optional
    """

    GOL: _GOL = Field(
        default=...,
        title="GOL",
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

    GOAL_ROLE: list[_PPR_PC1_GOAL_ROLE] | None = Field(
        default=None,
        title="GOAL_ROLE",
        description="Optional, repeating",
    )

    GOAL_OBSERVATION: list[_PPR_PC1_GOAL_OBSERVATION] | None = Field(
        default=None,
        title="GOAL_OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
