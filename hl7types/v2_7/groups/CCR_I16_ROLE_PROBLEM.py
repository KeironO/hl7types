"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: CCR_I16.ROLE_PROBLEM
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.VAR import VAR

from .CCR_I16_ROLE_PROBLEM_OBJECT import CCR_I16_ROLE_PROBLEM_OBJECT

_CCR_I16_ROLE_PROBLEM_OBJECT = CCR_I16_ROLE_PROBLEM_OBJECT
_VAR = VAR


class CCR_I16_ROLE_PROBLEM(BaseModel):
    """HL7 v2 CCR_I16.ROLE_PROBLEM group.

    Attributes:
        ROLE_PROBLEM_OBJECT (CCR_I16_ROLE_PROBLEM_OBJECT): required
        VAR (Optional[List[VAR]]): optional
    """

    ROLE_PROBLEM_OBJECT: _CCR_I16_ROLE_PROBLEM_OBJECT = Field(
        default=...,
        title="ROLE_PROBLEM_OBJECT",
        description="Required",
    )

    VAR: Optional[List[_VAR]] = Field(
        default=None,
        title="VAR",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
