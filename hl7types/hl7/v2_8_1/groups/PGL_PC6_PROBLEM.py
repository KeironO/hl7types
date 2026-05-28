"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: PGL_PC6.PROBLEM
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.PRB import PRB
from ..segments.VAR import VAR
from .PGL_PC6_PROBLEM_OBSERVATION import PGL_PC6_PROBLEM_OBSERVATION
from .PGL_PC6_PROBLEM_ROLE import PGL_PC6_PROBLEM_ROLE

_NTE = NTE
_PGL_PC6_PROBLEM_OBSERVATION = PGL_PC6_PROBLEM_OBSERVATION
_PGL_PC6_PROBLEM_ROLE = PGL_PC6_PROBLEM_ROLE
_PRB = PRB
_VAR = VAR


class PGL_PC6_PROBLEM(BaseModel):
    """HL7 v2 PGL_PC6.PROBLEM group.

    Attributes:
        PRB (PRB): required
        NTE (Optional[List[NTE]]): optional
        VAR (Optional[List[VAR]]): optional
        PROBLEM_ROLE (Optional[List[PGL_PC6_PROBLEM_ROLE]]): optional
        PROBLEM_OBSERVATION (Optional[List[PGL_PC6_PROBLEM_OBSERVATION]]): optional
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

    PROBLEM_ROLE: list[_PGL_PC6_PROBLEM_ROLE] | None = Field(
        default=None,
        title="PROBLEM_ROLE",
        description="Optional, repeating",
    )

    PROBLEM_OBSERVATION: list[_PGL_PC6_PROBLEM_OBSERVATION] | None = Field(
        default=None,
        title="PROBLEM_OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
