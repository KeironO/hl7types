"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: CCR_I16.ROLE_GOAL
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..segments.VAR import VAR
from .CCR_I16_ROLE_GOAL_OBJECT import CCR_I16_ROLE_GOAL_OBJECT

_CCR_I16_ROLE_GOAL_OBJECT = CCR_I16_ROLE_GOAL_OBJECT
_VAR = VAR


class CCR_I16_ROLE_GOAL(BaseModel):
    """HL7 v2 CCR_I16.ROLE_GOAL group.

    Attributes:
        ROLE_GOAL_OBJECT (CCR_I16_ROLE_GOAL_OBJECT): required
        VAR (Optional[List[VAR]]): optional
    """

    ROLE_GOAL_OBJECT: _CCR_I16_ROLE_GOAL_OBJECT = Field(
        default=...,
        title="ROLE_GOAL_OBJECT",
        description="Required",
    )

    VAR: list[_VAR] | None = Field(
        default=None,
        title="VAR",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
