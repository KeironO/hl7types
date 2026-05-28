"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: PTR_PCF.PROBLEM
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.PRB import PRB
from ..segments.VAR import VAR

from .PTR_PCF_GOAL import PTR_PCF_GOAL
from .PTR_PCF_ORDER import PTR_PCF_ORDER
from .PTR_PCF_PROBLEM_OBSERVATION import PTR_PCF_PROBLEM_OBSERVATION
from .PTR_PCF_PROBLEM_ROLE import PTR_PCF_PROBLEM_ROLE

_NTE = NTE
_PRB = PRB
_PTR_PCF_GOAL = PTR_PCF_GOAL
_PTR_PCF_ORDER = PTR_PCF_ORDER
_PTR_PCF_PROBLEM_OBSERVATION = PTR_PCF_PROBLEM_OBSERVATION
_PTR_PCF_PROBLEM_ROLE = PTR_PCF_PROBLEM_ROLE
_VAR = VAR


class PTR_PCF_PROBLEM(BaseModel):
    """HL7 v2 PTR_PCF.PROBLEM group.

    Attributes:
        PRB (PRB): required
        NTE (Optional[List[NTE]]): optional
        VAR (Optional[List[VAR]]): optional
        PROBLEM_ROLE (Optional[List[PTR_PCF_PROBLEM_ROLE]]): optional
        PROBLEM_OBSERVATION (Optional[List[PTR_PCF_PROBLEM_OBSERVATION]]): optional
        GOAL (Optional[List[PTR_PCF_GOAL]]): optional
        ORDER (Optional[List[PTR_PCF_ORDER]]): optional
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

    PROBLEM_ROLE: Optional[List[_PTR_PCF_PROBLEM_ROLE]] = Field(
        default=None,
        title="PROBLEM_ROLE",
        description="Optional, repeating",
    )

    PROBLEM_OBSERVATION: Optional[List[_PTR_PCF_PROBLEM_OBSERVATION]] = Field(
        default=None,
        title="PROBLEM_OBSERVATION",
        description="Optional, repeating",
    )

    GOAL: Optional[List[_PTR_PCF_GOAL]] = Field(
        default=None,
        title="GOAL",
        description="Optional, repeating",
    )

    ORDER: Optional[List[_PTR_PCF_ORDER]] = Field(
        default=None,
        title="ORDER",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
