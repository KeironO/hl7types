"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: CQU_I19.ROLE_PROBLEM
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.VAR import VAR

from .CQU_I19_ROLE_PROBLEM_OBJECT import CQU_I19_ROLE_PROBLEM_OBJECT

_CQU_I19_ROLE_PROBLEM_OBJECT = CQU_I19_ROLE_PROBLEM_OBJECT
_VAR = VAR


class CQU_I19_ROLE_PROBLEM(BaseModel):
    """HL7 v2 CQU_I19.ROLE_PROBLEM group.

    Attributes:
        ROLE_PROBLEM_OBJECT (CQU_I19_ROLE_PROBLEM_OBJECT): required
        VAR (Optional[List[VAR]]): optional
    """

    ROLE_PROBLEM_OBJECT: _CQU_I19_ROLE_PROBLEM_OBJECT = Field(
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
