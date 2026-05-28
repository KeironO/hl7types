"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: CCU_I20.GOAL
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.GOL import GOL
from ..segments.VAR import VAR
from .CCU_I20_GOAL_OBSERVATION import CCU_I20_GOAL_OBSERVATION
from .CCU_I20_ROLE_GOAL import CCU_I20_ROLE_GOAL

_CCU_I20_GOAL_OBSERVATION = CCU_I20_GOAL_OBSERVATION
_CCU_I20_ROLE_GOAL = CCU_I20_ROLE_GOAL
_GOL = GOL
_VAR = VAR


class CCU_I20_GOAL(BaseModel):
    """HL7 v2 CCU_I20.GOAL group.

    Attributes:
        GOL (GOL): required
        VAR (Optional[List[VAR]]): optional
        ROLE_GOAL (Optional[List[CCU_I20_ROLE_GOAL]]): optional
        GOAL_OBSERVATION (Optional[List[CCU_I20_GOAL_OBSERVATION]]): optional
    """

    GOL: _GOL = Field(
        default=...,
        title="GOL",
        description="Required",
    )

    VAR: list[_VAR] | None = Field(
        default=None,
        title="VAR",
        description="Optional, repeating",
    )

    ROLE_GOAL: list[_CCU_I20_ROLE_GOAL] | None = Field(
        default=None,
        title="ROLE_GOAL",
        description="Optional, repeating",
    )

    GOAL_OBSERVATION: list[_CCU_I20_GOAL_OBSERVATION] | None = Field(
        default=None,
        title="GOAL_OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
