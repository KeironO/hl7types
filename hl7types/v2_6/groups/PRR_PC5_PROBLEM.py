"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: PRR_PC5.PROBLEM
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.PRB import PRB
from ..segments.VAR import VAR

from .PRR_PC5_GOAL import PRR_PC5_GOAL
from .PRR_PC5_ORDER import PRR_PC5_ORDER
from .PRR_PC5_PROBLEM_OBSERVATION import PRR_PC5_PROBLEM_OBSERVATION
from .PRR_PC5_PROBLEM_PATHWAY import PRR_PC5_PROBLEM_PATHWAY
from .PRR_PC5_PROBLEM_ROLE import PRR_PC5_PROBLEM_ROLE

_NTE = NTE
_PRB = PRB
_PRR_PC5_GOAL = PRR_PC5_GOAL
_PRR_PC5_ORDER = PRR_PC5_ORDER
_PRR_PC5_PROBLEM_OBSERVATION = PRR_PC5_PROBLEM_OBSERVATION
_PRR_PC5_PROBLEM_PATHWAY = PRR_PC5_PROBLEM_PATHWAY
_PRR_PC5_PROBLEM_ROLE = PRR_PC5_PROBLEM_ROLE
_VAR = VAR


class PRR_PC5_PROBLEM(BaseModel):
    """HL7 v2 PRR_PC5.PROBLEM group.

    Attributes:
        PRB (PRB): required
        NTE (Optional[List[NTE]]): optional
        VAR (Optional[List[VAR]]): optional
        PROBLEM_ROLE (Optional[List[PRR_PC5_PROBLEM_ROLE]]): optional
        PROBLEM_PATHWAY (Optional[List[PRR_PC5_PROBLEM_PATHWAY]]): optional
        PROBLEM_OBSERVATION (Optional[List[PRR_PC5_PROBLEM_OBSERVATION]]): optional
        GOAL (Optional[List[PRR_PC5_GOAL]]): optional
        ORDER (Optional[List[PRR_PC5_ORDER]]): optional
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

    PROBLEM_ROLE: Optional[List[_PRR_PC5_PROBLEM_ROLE]] = Field(
        default=None,
        title="PROBLEM_ROLE",
        description="Optional, repeating",
    )

    PROBLEM_PATHWAY: Optional[List[_PRR_PC5_PROBLEM_PATHWAY]] = Field(
        default=None,
        title="PROBLEM_PATHWAY",
        description="Optional, repeating",
    )

    PROBLEM_OBSERVATION: Optional[List[_PRR_PC5_PROBLEM_OBSERVATION]] = Field(
        default=None,
        title="PROBLEM_OBSERVATION",
        description="Optional, repeating",
    )

    GOAL: Optional[List[_PRR_PC5_GOAL]] = Field(
        default=None,
        title="GOAL",
        description="Optional, repeating",
    )

    ORDER: Optional[List[_PRR_PC5_ORDER]] = Field(
        default=None,
        title="ORDER",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
