"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: CCI_I22.ROLE_GOAL
Type: Group
"""
from _future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.VAR import VAR

from .CCI_I22_ROLE_GOAL_OBJECT import CCI_I22_ROLE_GOAL_OBJECT

_CCI_I22_ROLE_GOAL_OBJECT = CCI_I22_ROLE_GOAL_OBJECT
_VAR = VAR


class CCI_I22_ROLE_GOAL(BaseModel):
    """HL7 v2 CCI_I22.ROLE_GOAL group.

    Attributes:
        ROLE_GOAL_OBJECT (CCI_I22_ROLE_GOAL_OBJECT): required
        VAR (Optional[List[VAR]]): optional
    """

    ROLE_GOAL_OBJECT: _CCI_I22_ROLE_GOAL_OBJECT = Field(
        default=...,
        title="ROLE_GOAL_OBJECT",
        description="Required",
    )

    VAR: Optional[List[_VAR]] = Field(
        default=None,
        title="VAR",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
