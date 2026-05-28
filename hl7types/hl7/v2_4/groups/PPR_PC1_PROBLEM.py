"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: PPR_PC1.PROBLEM
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.PRB import PRB
from ..segments.VAR import VAR

from .PPR_PC1_GOAL import PPR_PC1_GOAL
from .PPR_PC1_ORDER import PPR_PC1_ORDER
from .PPR_PC1_PATHWAY import PPR_PC1_PATHWAY
from .PPR_PC1_PROBLEM_OBSERVATION import PPR_PC1_PROBLEM_OBSERVATION
from .PPR_PC1_PROBLEM_ROLE import PPR_PC1_PROBLEM_ROLE

_NTE = NTE
_PPR_PC1_GOAL = PPR_PC1_GOAL
_PPR_PC1_ORDER = PPR_PC1_ORDER
_PPR_PC1_PATHWAY = PPR_PC1_PATHWAY
_PPR_PC1_PROBLEM_OBSERVATION = PPR_PC1_PROBLEM_OBSERVATION
_PPR_PC1_PROBLEM_ROLE = PPR_PC1_PROBLEM_ROLE
_PRB = PRB
_VAR = VAR


class PPR_PC1_PROBLEM(BaseModel):
    """HL7 v2 PPR_PC1.PROBLEM group.

    Attributes:
        PRB (PRB): required
        NTE (Optional[List[NTE]]): optional
        VAR (Optional[List[VAR]]): optional
        PROBLEM_ROLE (Optional[List[PPR_PC1_PROBLEM_ROLE]]): optional
        PATHWAY (Optional[List[PPR_PC1_PATHWAY]]): optional
        PROBLEM_OBSERVATION (Optional[List[PPR_PC1_PROBLEM_OBSERVATION]]): optional
        GOAL (Optional[List[PPR_PC1_GOAL]]): optional
        ORDER (Optional[List[PPR_PC1_ORDER]]): optional
    """

    PRB: _PRB = Field(
        default=...,
        title="PRB",
        description="Required",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Optional, repeating",
    )

    VAR: Optional[List[_VAR]] = Field(
        default=None,
        title="VAR",
        description="Optional, repeating",
    )

    PROBLEM_ROLE: Optional[List[_PPR_PC1_PROBLEM_ROLE]] = Field(
        default=None,
        title="PROBLEM_ROLE",
        description="Optional, repeating",
    )

    PATHWAY: Optional[List[_PPR_PC1_PATHWAY]] = Field(
        default=None,
        title="PATHWAY",
        description="Optional, repeating",
    )

    PROBLEM_OBSERVATION: Optional[List[_PPR_PC1_PROBLEM_OBSERVATION]] = Field(
        default=None,
        title="PROBLEM_OBSERVATION",
        description="Optional, repeating",
    )

    GOAL: Optional[List[_PPR_PC1_GOAL]] = Field(
        default=None,
        title="GOAL",
        description="Optional, repeating",
    )

    ORDER: Optional[List[_PPR_PC1_ORDER]] = Field(
        default=None,
        title="ORDER",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
