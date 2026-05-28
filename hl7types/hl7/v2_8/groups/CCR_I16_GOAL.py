"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: CCR_I16.GOAL
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.GOL import GOL
from ..segments.VAR import VAR
from .CCR_I16_GOAL_OBSERVATION import CCR_I16_GOAL_OBSERVATION
from .CCR_I16_ROLE_GOAL import CCR_I16_ROLE_GOAL

_CCR_I16_GOAL_OBSERVATION = CCR_I16_GOAL_OBSERVATION
_CCR_I16_ROLE_GOAL = CCR_I16_ROLE_GOAL
_GOL = GOL
_VAR = VAR


class CCR_I16_GOAL(BaseModel):
    """HL7 v2 CCR_I16.GOAL group.

    Attributes:
        GOL (GOL): required
        VAR (Optional[List[VAR]]): optional
        ROLE_GOAL (Optional[List[CCR_I16_ROLE_GOAL]]): optional
        GOAL_OBSERVATION (Optional[List[CCR_I16_GOAL_OBSERVATION]]): optional
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

    ROLE_GOAL: list[_CCR_I16_ROLE_GOAL] | None = Field(
        default=None,
        title="ROLE_GOAL",
        description="Optional, repeating",
    )

    GOAL_OBSERVATION: list[_CCR_I16_GOAL_OBSERVATION] | None = Field(
        default=None,
        title="GOAL_OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
