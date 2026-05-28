"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: PRR_PC5.GOAL
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.GOL import GOL
from ..segments.NTE import NTE
from ..segments.VAR import VAR
from .PRR_PC5_GOAL_OBSERVATION import PRR_PC5_GOAL_OBSERVATION
from .PRR_PC5_GOAL_ROLE import PRR_PC5_GOAL_ROLE

_GOL = GOL
_NTE = NTE
_PRR_PC5_GOAL_OBSERVATION = PRR_PC5_GOAL_OBSERVATION
_PRR_PC5_GOAL_ROLE = PRR_PC5_GOAL_ROLE
_VAR = VAR


class PRR_PC5_GOAL(BaseModel):
    """HL7 v2 PRR_PC5.GOAL group.

    Attributes:
        GOL (GOL): required
        NTE (Optional[List[NTE]]): optional
        VAR (Optional[List[VAR]]): optional
        GOAL_ROLE (Optional[List[PRR_PC5_GOAL_ROLE]]): optional
        GOAL_OBSERVATION (Optional[List[PRR_PC5_GOAL_OBSERVATION]]): optional
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

    GOAL_ROLE: list[_PRR_PC5_GOAL_ROLE] | None = Field(
        default=None,
        title="GOAL_ROLE",
        description="Optional, repeating",
    )

    GOAL_OBSERVATION: list[_PRR_PC5_GOAL_OBSERVATION] | None = Field(
        default=None,
        title="GOAL_OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
