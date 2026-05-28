"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: PPP_PCB.PROBLEM
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.PRB import PRB
from ..segments.VAR import VAR
from .PPP_PCB_GOAL import PPP_PCB_GOAL
from .PPP_PCB_ORDER import PPP_PCB_ORDER
from .PPP_PCB_PROBLEM_OBSERVATION import PPP_PCB_PROBLEM_OBSERVATION
from .PPP_PCB_PROBLEM_ROLE import PPP_PCB_PROBLEM_ROLE

_NTE = NTE
_PPP_PCB_GOAL = PPP_PCB_GOAL
_PPP_PCB_ORDER = PPP_PCB_ORDER
_PPP_PCB_PROBLEM_OBSERVATION = PPP_PCB_PROBLEM_OBSERVATION
_PPP_PCB_PROBLEM_ROLE = PPP_PCB_PROBLEM_ROLE
_PRB = PRB
_VAR = VAR


class PPP_PCB_PROBLEM(BaseModel):
    """HL7 v2 PPP_PCB.PROBLEM group.

    Attributes:
        PRB (PRB): required
        NTE (Optional[List[NTE]]): optional
        VAR (Optional[List[VAR]]): optional
        PROBLEM_ROLE (Optional[List[PPP_PCB_PROBLEM_ROLE]]): optional
        PROBLEM_OBSERVATION (Optional[List[PPP_PCB_PROBLEM_OBSERVATION]]): optional
        GOAL (Optional[List[PPP_PCB_GOAL]]): optional
        ORDER (Optional[List[PPP_PCB_ORDER]]): optional
    """

    PRB: _PRB = Field(
        default=...,
        title="PRB",
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

    PROBLEM_ROLE: list[_PPP_PCB_PROBLEM_ROLE] | None = Field(
        default=None,
        title="PROBLEM_ROLE",
        description="Optional, repeating",
    )

    PROBLEM_OBSERVATION: list[_PPP_PCB_PROBLEM_OBSERVATION] | None = Field(
        default=None,
        title="PROBLEM_OBSERVATION",
        description="Optional, repeating",
    )

    GOAL: list[_PPP_PCB_GOAL] | None = Field(
        default=None,
        title="GOAL",
        description="Optional, repeating",
    )

    ORDER: list[_PPP_PCB_ORDER] | None = Field(
        default=None,
        title="ORDER",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
