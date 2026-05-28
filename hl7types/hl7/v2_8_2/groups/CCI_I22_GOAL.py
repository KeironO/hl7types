"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: CCI_I22.GOAL
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.GOL import GOL
from ..segments.VAR import VAR
from .CCI_I22_GOAL_OBSERVATION import CCI_I22_GOAL_OBSERVATION
from .CCI_I22_ROLE_GOAL import CCI_I22_ROLE_GOAL

_CCI_I22_GOAL_OBSERVATION = CCI_I22_GOAL_OBSERVATION
_CCI_I22_ROLE_GOAL = CCI_I22_ROLE_GOAL
_GOL = GOL
_VAR = VAR


class CCI_I22_GOAL(BaseModel):
    """HL7 v2 CCI_I22.GOAL group.

    Attributes:
        GOL (GOL): required
        VAR (Optional[List[VAR]]): optional
        ROLE_GOAL (Optional[List[CCI_I22_ROLE_GOAL]]): optional
        GOAL_OBSERVATION (Optional[List[CCI_I22_GOAL_OBSERVATION]]): optional
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

    ROLE_GOAL: list[_CCI_I22_ROLE_GOAL] | None = Field(
        default=None,
        title="ROLE_GOAL",
        description="Optional, repeating",
    )

    GOAL_OBSERVATION: list[_CCI_I22_GOAL_OBSERVATION] | None = Field(
        default=None,
        title="GOAL_OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
