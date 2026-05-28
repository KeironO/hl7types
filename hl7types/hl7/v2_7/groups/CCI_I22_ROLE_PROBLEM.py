"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: CCI_I22.ROLE_PROBLEM
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.VAR import VAR
from .CCI_I22_ROLE_PROBLEM_OBJECT import CCI_I22_ROLE_PROBLEM_OBJECT

_CCI_I22_ROLE_PROBLEM_OBJECT = CCI_I22_ROLE_PROBLEM_OBJECT
_VAR = VAR


class CCI_I22_ROLE_PROBLEM(BaseModel):
    """HL7 v2 CCI_I22.ROLE_PROBLEM group.

    Attributes:
        ROLE_PROBLEM_OBJECT (CCI_I22_ROLE_PROBLEM_OBJECT): required
        VAR (Optional[List[VAR]]): optional
    """

    ROLE_PROBLEM_OBJECT: _CCI_I22_ROLE_PROBLEM_OBJECT = Field(
        default=...,
        title="ROLE_PROBLEM_OBJECT",
        description="Required",
    )

    VAR: list[_VAR] | None = Field(
        default=None,
        title="VAR",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
