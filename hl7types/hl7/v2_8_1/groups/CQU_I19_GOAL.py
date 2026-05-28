"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: CQU_I19.GOAL
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import BaseModel, Field

from ..segments.GOL import GOL
from ..segments.VAR import VAR

from .CQU_I19_GOAL_OBSERVATION import CQU_I19_GOAL_OBSERVATION
from .CQU_I19_ROLE_GOAL import CQU_I19_ROLE_GOAL

_CQU_I19_GOAL_OBSERVATION = CQU_I19_GOAL_OBSERVATION
_CQU_I19_ROLE_GOAL = CQU_I19_ROLE_GOAL
_GOL = GOL
_VAR = VAR


class CQU_I19_GOAL(BaseModel):
    """HL7 v2 CQU_I19.GOAL group.

    Attributes:
        GOL (GOL): required
        VAR (Optional[List[VAR]]): optional
        ROLE_GOAL (Optional[List[CQU_I19_ROLE_GOAL]]): optional
        GOAL_OBSERVATION (Optional[List[CQU_I19_GOAL_OBSERVATION]]): optional
    """

    GOL: _GOL = Field(
        default=...,
        title="GOL",
        description="Required",
    )

    VAR: Optional[List[_VAR]] = Field(
        default=None,
        title="VAR",
        description="Optional, repeating",
    )

    ROLE_GOAL: Optional[List[_CQU_I19_ROLE_GOAL]] = Field(
        default=None,
        title="ROLE_GOAL",
        description="Optional, repeating",
    )

    GOAL_OBSERVATION: Optional[List[_CQU_I19_GOAL_OBSERVATION]] = Field(
        default=None,
        title="GOAL_OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
