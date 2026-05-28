"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: CCU_I20.PROBLEM
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.PRB import PRB
from ..segments.VAR import VAR

from .CCU_I20_PROBLEM_OBSERVATION import CCU_I20_PROBLEM_OBSERVATION
from .CCU_I20_ROLE_PROBLEM import CCU_I20_ROLE_PROBLEM

_CCU_I20_PROBLEM_OBSERVATION = CCU_I20_PROBLEM_OBSERVATION
_CCU_I20_ROLE_PROBLEM = CCU_I20_ROLE_PROBLEM
_PRB = PRB
_VAR = VAR


class CCU_I20_PROBLEM(BaseModel):
    """HL7 v2 CCU_I20.PROBLEM group.

    Attributes:
        PRB (PRB): required
        VAR (Optional[List[VAR]]): optional
        ROLE_PROBLEM (Optional[List[CCU_I20_ROLE_PROBLEM]]): optional
        PROBLEM_OBSERVATION (Optional[List[CCU_I20_PROBLEM_OBSERVATION]]): optional
    """

    PRB: _PRB = Field(
        default=...,
        title="PRB",
        description="Required",
    )

    VAR: Optional[List[_VAR]] = Field(
        default=None,
        title="VAR",
        description="Optional, repeating",
    )

    ROLE_PROBLEM: Optional[List[_CCU_I20_ROLE_PROBLEM]] = Field(
        default=None,
        title="ROLE_PROBLEM",
        description="Optional, repeating",
    )

    PROBLEM_OBSERVATION: Optional[List[_CCU_I20_PROBLEM_OBSERVATION]] = Field(
        default=None,
        title="PROBLEM_OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
