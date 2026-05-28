"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: PPT_PCL.PROBLEM
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.NTE import NTE
from ..segments.PRB import PRB
from ..segments.VAR import VAR
from .PPT_PCL_PROBLEM_OBSERVATION import PPT_PCL_PROBLEM_OBSERVATION
from .PPT_PCL_PROBLEM_ROLE import PPT_PCL_PROBLEM_ROLE

_NTE = NTE
_PPT_PCL_PROBLEM_OBSERVATION = PPT_PCL_PROBLEM_OBSERVATION
_PPT_PCL_PROBLEM_ROLE = PPT_PCL_PROBLEM_ROLE
_PRB = PRB
_VAR = VAR


class PPT_PCL_PROBLEM(BaseModel):
    """HL7 v2 PPT_PCL.PROBLEM group.

    Attributes:
        PRB (PRB): required
        NTE (Optional[List[NTE]]): optional
        VAR (Optional[List[VAR]]): optional
        PROBLEM_ROLE (Optional[List[PPT_PCL_PROBLEM_ROLE]]): optional
        PROBLEM_OBSERVATION (Optional[List[PPT_PCL_PROBLEM_OBSERVATION]]): optional
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

    PROBLEM_ROLE: list[_PPT_PCL_PROBLEM_ROLE] | None = Field(
        default=None,
        title="PROBLEM_ROLE",
        description="Optional, repeating",
    )

    PROBLEM_OBSERVATION: list[_PPT_PCL_PROBLEM_OBSERVATION] | None = Field(
        default=None,
        title="PROBLEM_OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
