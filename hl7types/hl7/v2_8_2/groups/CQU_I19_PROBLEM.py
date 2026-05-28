"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: CQU_I19.PROBLEM
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.PRB import PRB
from ..segments.VAR import VAR
from .CQU_I19_PROBLEM_OBSERVATION import CQU_I19_PROBLEM_OBSERVATION
from .CQU_I19_ROLE_PROBLEM import CQU_I19_ROLE_PROBLEM

_CQU_I19_PROBLEM_OBSERVATION = CQU_I19_PROBLEM_OBSERVATION
_CQU_I19_ROLE_PROBLEM = CQU_I19_ROLE_PROBLEM
_PRB = PRB
_VAR = VAR


class CQU_I19_PROBLEM(BaseModel):
    """HL7 v2 CQU_I19.PROBLEM group.

    Attributes:
        PRB (PRB): required
        VAR (Optional[List[VAR]]): optional
        ROLE_PROBLEM (Optional[List[CQU_I19_ROLE_PROBLEM]]): optional
        PROBLEM_OBSERVATION (Optional[List[CQU_I19_PROBLEM_OBSERVATION]]): optional
    """

    PRB: _PRB = Field(
        default=...,
        title="PRB",
        description="Required",
    )

    VAR: list[_VAR] | None = Field(
        default=None,
        title="VAR",
        description="Optional, repeating",
    )

    ROLE_PROBLEM: list[_CQU_I19_ROLE_PROBLEM] | None = Field(
        default=None,
        title="ROLE_PROBLEM",
        description="Optional, repeating",
    )

    PROBLEM_OBSERVATION: list[_CQU_I19_PROBLEM_OBSERVATION] | None = Field(
        default=None,
        title="PROBLEM_OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
