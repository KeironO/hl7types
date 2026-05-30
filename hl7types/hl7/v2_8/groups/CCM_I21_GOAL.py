"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: CCM_I21.GOAL
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.GOL import GOL
from ..segments.VAR import VAR

from .CCM_I21_GOAL_OBSERVATION import CCM_I21_GOAL_OBSERVATION
from .CCM_I21_ROLE_GOAL import CCM_I21_ROLE_GOAL

_CCM_I21_GOAL_OBSERVATION = CCM_I21_GOAL_OBSERVATION
_CCM_I21_ROLE_GOAL = CCM_I21_ROLE_GOAL
_GOL = GOL
_VAR = VAR


class CCM_I21_GOAL(HL7Model):
    """HL7 v2 CCM_I21.GOAL group.

    Attributes:
        GOL (GOL): required
        VAR (Optional[List[VAR]]): optional
        ROLE_GOAL (Optional[List[CCM_I21_ROLE_GOAL]]): optional
        GOAL_OBSERVATION (Optional[List[CCM_I21_GOAL_OBSERVATION]]): optional
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

    ROLE_GOAL: Optional[List[_CCM_I21_ROLE_GOAL]] = Field(
        default=None,
        title="ROLE_GOAL",
        description="Optional, repeating",
    )

    GOAL_OBSERVATION: Optional[List[_CCM_I21_GOAL_OBSERVATION]] = Field(
        default=None,
        title="GOAL_OBSERVATION",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
