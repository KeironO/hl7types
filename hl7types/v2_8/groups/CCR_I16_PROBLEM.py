"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: CCR_I16.PROBLEM
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.PRB import PRB
from ..segments.VAR import VAR

from .CCR_I16_ROLE_OBSERVATION import CCR_I16_ROLE_OBSERVATION
from .CCR_I16_ROLE_PROBLEM import CCR_I16_ROLE_PROBLEM

_CCR_I16_ROLE_OBSERVATION = CCR_I16_ROLE_OBSERVATION
_CCR_I16_ROLE_PROBLEM = CCR_I16_ROLE_PROBLEM
_PRB = PRB
_VAR = VAR


class CCR_I16_PROBLEM(BaseModel):
    """HL7 v2 CCR_I16.PROBLEM group.

    Attributes:
        PRB (PRB): required
        VAR (Optional[List[VAR]]): optional
        ROLE_PROBLEM (Optional[List[CCR_I16_ROLE_PROBLEM]]): optional
        ROLE_OBSERVATION (Optional[List[CCR_I16_ROLE_OBSERVATION]]): optional
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

    ROLE_PROBLEM: Optional[List[_CCR_I16_ROLE_PROBLEM]] = Field(
        default=None,
        title="ROLE_PROBLEM",
        description="Optional, repeating",
    )

    ROLE_OBSERVATION: Optional[List[_CCR_I16_ROLE_OBSERVATION]] = Field(
        default=None,
        title="ROLE_OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
